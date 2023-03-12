from bs4 import BeautifulSoup, Tag

from app.clients.client import Client
from app.schemas.clients import HhResume, Education, WorkExperience


class HhClient:
    def __init__(self, client: Client):
        self._client = client

    async def get_resume(self, url: str) -> HhResume:
        response = await self._client.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')

        resume_title = soup.find(class_='resume-header-title')
        name_tag = resume_title.find(class_='bloko-header-1')
        first_name, last_name, middle_name = self._get_name(name_tag)

        phone_tag = resume_title.find(attrs={'data-qa': 'resume-contacts-phone'})
        phone = self._get_phone(phone_tag)

        email_tag = resume_title.find(attrs={'data-qa': 'resume-contact-email'})
        email = self._get_email(email_tag)

        education_tag = soup.find(class_='resume-block', attrs={'data-qa': 'resume-block-education'})
        education = self._get_education(education_tag)

        experience_tag = soup.find(class_='resume-block', attrs={'data-qa': 'resume-block-experience'})
        experience = self._get_experience(experience_tag)

        return HhResume(
            first_name=first_name,
            last_name=last_name,
            middle_name=middle_name,
            phone=phone,
            email=email,
            education=education,
            work_experience=experience
        )

    def _get_name(self, name: Tag | None) -> tuple[str | None, str | None, str | None]:
        if name is None:
            return None, None, None

        full_name = name.text.split(" ")
        if len(full_name) > 2:
            last_name, first_name, middle_name = full_name
        else:
            last_name, first_name = full_name
            middle_name = None

        return first_name, last_name, middle_name

    def _get_phone(self, phone: Tag | None) -> str | None:
        try:
            return phone.span.text
        except AttributeError:
            return None

    def _get_email(self, email: Tag | None) -> str | None:
        try:
            return email.a.text
        except AttributeError:
            return None

    def _get_education(self, education_tag: Tag | None) -> list[Education]:
        if education_tag is None:
            return []

        educations = []
        for elem in education_tag.findAll(class_='resume-block-item-gap')[1:]:
            try:
                year = elem.find(
                    class_='bloko-column bloko-column_xs-4 bloko-column_s-2 bloko-column_m-2 bloko-column_l-2').text
                university = elem.find(
                    class_='bloko-column bloko-column_xs-4 bloko-column_s-6 bloko-column_m-7 bloko-column_l-10').text

                educations.append(Education(year=year, university=university))
            except AttributeError:
                pass

        return educations

    def _get_experience(self, experience_tag: Tag | None) -> list[WorkExperience]:
        if experience_tag is None:
            return []

        experiences = []
        for elem in experience_tag.findAll(class_='resume-block-item-gap')[1:]:
            try:
                year = elem.find(
                    class_='bloko-column bloko-column_xs-4 bloko-column_s-2 bloko-column_m-2 bloko-column_l-2').text
                experience = elem.find(
                    class_='bloko-column bloko-column_xs-4 bloko-column_s-6 bloko-column_m-7 bloko-column_l-10').text

                experiences.append(WorkExperience(year=year, experience=experience))
            except AttributeError:
                pass

        return experiences
