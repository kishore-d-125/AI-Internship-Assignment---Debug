## Importing libraries and files
import os
from dotenv import load_dotenv
load_dotenv()

from langchain_community.document_loaders import PyPDFLoader

## Creating custom pdf reader tool
class BloodTestReportTool():
    def read_data_tool(self, path='data/sample.pdf'):
        """Tool to read data from a pdf file from a path

        Args:
            path (str, optional): Path of the pdf file. Defaults to 'data/sample.pdf'.

        Returns:
            str: Full Blood Test report file
        """
        try:
            docs = PyPDFLoader(file_path=path).load()

            full_report = ""
            for data in docs:
                # Clean and format the text
                text = data.page_content.strip()
                full_report += text + "\n\n"

            return full_report
        except Exception as e:
            return f"Error reading PDF file: {str(e)}"

# Create a simple search tool placeholder
class SimpleSearchTool():
    def search(self, query):
        """Simple search tool placeholder"""
        return f"Search results for: {query} (Note: Web search functionality requires crewai_tools)"

# Initialize tools
blood_test_tool = BloodTestReportTool()
search_tool = SimpleSearchTool()

## Creating Nutrition Analysis Tool
class NutritionTool:
    def analyze_nutrition_tool(self, blood_report_data):
        # Process and analyze the blood report data
        processed_data = blood_report_data
        
        # Clean up the data format
        i = 0
        while i < len(processed_data):
            if processed_data[i:i+2] == "  ":  # Remove double spaces
                processed_data = processed_data[:i] + processed_data[i+1:]
            else:
                i += 1
                
        # TODO: Implement nutrition analysis logic here
        return "Nutrition analysis functionality to be implemented"

## Creating Exercise Planning Tool
class ExerciseTool:
    def create_exercise_plan_tool(self, blood_report_data):        
        # TODO: Implement exercise planning logic here
        return "Exercise planning functionality to be implemented"