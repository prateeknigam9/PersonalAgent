from configuration_file import configure_gmail_connection, setup_environment
from crewai import Agent, Task, Crew, LLM, Process


setup_environment()
api_resource = configure_gmail_connection()

from crewai.tools import BaseTool
from pydantic import BaseModel, Field
from typing import Optional, Type
import json
import os

# Define the contact schema as provided
class ContactSchema(BaseModel):
    name: str = Field(..., description="The name of person")
    relation: Optional[str] = Field(None, description="relationship with the person")
    email: Optional[str] = Field(..., description="email id of the person")
    phone: Optional[str] = Field(..., description="Mobile number of the person")

# Custom tool class
class ContactJsonFillerTool(BaseTool):
    name: str = "Contact JSON Filler"
    description: str = "A tool that fills contact information into a JSON file based on input data"

    def _run(self, input_data: dict) -> str:
        """
        Run the tool with input data and save to JSON file
        Args:
            input_data: Dictionary containing contact information
        Returns:
            String message indicating success or failure
        """
        try:
            # Validate input data against schema
            contact = ContactSchema(**input_data)
            
            # Read existing contacts
            with open("contacts.json", 'r') as f:
                contacts = json.load(f)
            
            # Convert contact to dict and append to list
            contact_dict = contact.dict(exclude_none=True)
            contacts.append(contact_dict)
            
            # Write updated contacts back to file
            with open("contacts.json", 'w') as f:
                json.dump(contacts, f, indent=4)
            
            return f"Successfully added contact {contact.name} to contacts.json"
        
        except Exception as e:
            return f"Error processing contact data: {str(e)}"

    def _validate_input(self, input_data: dict) -> bool:
        """Validate if required fields are present"""
        required_fields = {'name', 'email', 'phone'}
        return all(field in input_data for field in required_fields)

# Example usage
if __name__ == "__main__":
    # Create instance of the tool
    contact_tool = ContactJsonFillerTool()
    
    # Example input data
    sample_contact = {
        "name": "Supriya Gopinath",
        "relation": "girlfriend",
        "email": "supriya@prateek.com",
        "phone": "+1-555-123-4567"
    }
    
    # Run the tool
    result = contact_tool._run(sample_contact)
    print(result)











    

