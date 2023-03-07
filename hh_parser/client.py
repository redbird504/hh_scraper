import aiohttp
from typing import List, Tuple
from bs4 import BeautifulSoup, Tag
from hh_parser.resume import Resume


class HhClient:
    def __init__(self):
        self._headers = {
            'user-agent': 'Mozilla/5.0'
        }

    async def get_resume(self, url: str) -> Resume | None:
        async with aiohttp.ClientSession() as session:
            async with session.get(url=url, headers=self._headers) as response:
                if response.status != 200:
                    return None

                response_text = await response.text()
                soup = BeautifulSoup(response_text, 'html.parser')

                resume_title = soup.find(class_='resume-header-title')
                name_tag = resume_title.find(class_='bloko-header-1')
                first_name, last_name, middle_name = self._parse_name(name_tag)

                phone_tag = resume_title.find(attrs={'data-qa': 'resume-contacts-phone'})
                phone = self._parse_phone(phone_tag)

                email_tag = resume_title.find(attrs={'data-qa': 'resume-contact-email'})
                email = self._parse_email(email_tag)

                education_tag = soup.find(class_='resume-block', attrs={'data-qa': 'resume-block-education'})
                education = self._parse_education(education_tag)

                experience_tag = soup.find(class_='resume-block', attrs={'data-qa': 'resume-block-experience'})
                experience = self._parse_experience(experience_tag)

                return Resume(
                    first_name=first_name,
                    last_name=last_name,
                    middle_name=middle_name,
                    phone=phone,
                    email=email,
                    education=education,
                    experience=experience
                )

    def _parse_name(self, name: Tag | None) -> Tuple[str | None, str | None, str | None]:
        if name is None:
            return None, None, None

        full_name = name.text.split(" ")
        if len(full_name) > 2:
            last_name, first_name, middle_name = full_name
        else:
            last_name, first_name = full_name
            middle_name = None

        return first_name, last_name, middle_name

    def _parse_phone(self, phone: Tag | None) -> str | None:
        try:
            return phone.span.text
        except AttributeError:
            return None

    def _parse_email(self, email: Tag | None):
        try:
            return email.a.text
        except AttributeError:
            return None

    def _parse_education(self, education_tag: Tag | None) -> List[Tuple[str, str]]:
        educations = []
        for elem in education_tag.findAll(class_='resume-block-item-gap')[1:]:
            try:
                year = elem.find(
                    class_='bloko-column bloko-column_xs-4 bloko-column_s-2 bloko-column_m-2 bloko-column_l-2').text
                university = elem.find(
                    class_='bloko-column bloko-column_xs-4 bloko-column_s-6 bloko-column_m-7 bloko-column_l-10').text
                educations.append((year, university))
            except AttributeError:
                pass

        return educations

    def _parse_experience(self, experience_tag: Tag | None) -> List[Tuple[str, str]]:
        experiences = []
        for elem in experience_tag.findAll(class_='resume-block-item-gap')[1:]:
            try:
                year = elem.find(
                    class_='bloko-column bloko-column_xs-4 bloko-column_s-2 bloko-column_m-2 bloko-column_l-2').text
                experience = elem.find(
                    class_='bloko-column bloko-column_xs-4 bloko-column_s-6 bloko-column_m-7 bloko-column_l-10').text
                experiences.append((year, experience))

            except AttributeError:
                pass

        return experiences
