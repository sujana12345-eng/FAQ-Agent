from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher


class ActionInternshipRequirements(Action):
    def name(self) -> Text:
        return "action_internship_requirements"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        # Example dynamic reply — replace with logic or DB lookups as needed
        text = (
            "Typical requirements: be an enrolled student or recent graduate, "
            "have relevant coursework or projects, a resume, and sometimes a cover letter or portfolio. "
            "If you tell me the program name, I can provide more specific requirements."
        )

        dispatcher.utter_message(text=text)
        return []
