# from fastapi import FastAPI, HTTPException
# from pydantic import BaseModel
# from typing import Dict, Any
# from rasa_sdk import Tracker, Action
# from rasa_sdk.executor import CollectingDispatcher
# from .actions import ActionCheckFlightStatus, ActionCheckAirlineStatus, ActionScanQRCode, ActionNavigateToLocation

# app = FastAPI()

# class FlightStatusRequest(BaseModel):
#     flight_number: str

# class AirlineStatusRequest(BaseModel):
#     airline: str

# class QRCodeScanRequest(BaseModel):
#     pass

# class NavigationRequest(BaseModel):
#     intent: str

# def run_action(action: Action, slots: Dict[str, Any], latest_message: Dict[str, Any]) -> str:
#     tracker = Tracker(
#         sender_id='default',
#         slots=slots,
#         latest_message=latest_message,
#         events=[],
#         paused=False,
#         followup_action=None,
#         active_loop={},
#         latest_action_name=None
#     )
#     dispatcher = CollectingDispatcher()
#     domain = {}

#     action.run(dispatcher, tracker, domain)
#     messages = dispatcher.messages
#     if messages:
#         return messages[0]["text"]
#     else:
#         return "No relevant information found."

# @app.post("/check_flight_status")
# async def check_flight_status(request: FlightStatusRequest):
#     action = ActionCheckFlightStatus()
#     result = run_action(action, {"flight_number": request.flight_number}, {})
#     return {"message": result}

# @app.post("/check_airline_status")
# async def check_airline_status(request: AirlineStatusRequest):
#     action = ActionCheckAirlineStatus()
#     result = run_action(action, {"airline": request.airline}, {})
#     return {"message": result}

# @app.post("/scan_qr_code")
# async def scan_qr_code(request: QRCodeScanRequest):
#     action = ActionScanQRCode()
#     result = run_action(action, {}, {})
#     return {"message": result}

# @app.post("/navigate_to_location")
# async def navigate_to_location(request: NavigationRequest):
#     action = ActionNavigateToLocation()
#     result = run_action(action, {}, {"intent": {"name": request.intent}})
#     return {"message": result}

# if __name__ == "__main__":
#     import uvicorn
#     uvicorn.run("actions.api_server:app", host="127.0.0.1", port=8000, reload=True)
