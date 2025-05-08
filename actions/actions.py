from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

class ActionGreet(Action):
    def name(self) -> Text:
        return "action_greet"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(text="Hello! How can I assist you today?")
        return []

class ActionCheckBalance(Action):
    def name(self) -> Text:
        return "action_check_balance"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(text="Your current account balance is $1,245.67.")
        return []

class ActionTransferConfirm(Action):
    def name(self) -> Text:
        return "action_transfer_confirm"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        amount = tracker.get_slot("amount")
        person = tracker.get_slot("person")
        dispatcher.utter_message(text=f"Transferring {amount} to {person}. Is that correct?")
        return []

class ActionPayBill(Action):
    def name(self) -> Text:
        return "action_pay_bill"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(text="Your bill has been paid successfully.")
        return []

class ActionReportLostCardConfirm(Action):
    def name(self) -> Text:
        return "action_report_lost_card_confirm"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        address = tracker.get_slot("address")
        dispatcher.utter_message(text=f"Thank you for confirming your address of {address}. We will have your new card to you in 1-3 business days.")
        return []

class ActionTransactionHistory(Action):
    def name(self) -> Text:
        return "action_transaction_history"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(text="Here are your last three transactions: $50 at Amazon, $12 at Starbucks, $100 at Walmart.")
        return []

class ActionRequestStatement(Action):
    def name(self) -> Text:
        return "action_request_statement"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(text="Your requested statement has been emailed to you.")
        return []

class ActionTalkToHuman(Action):
    def name(self) -> Text:
        return "action_talk_to_human"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(text="Connecting you to a live representative. Please hold.")
        return []

class ActionGoodbye(Action):
    def name(self) -> Text:
        return "action_goodbye"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(text="Goodbye. Thank you for using our service.")
        return []
