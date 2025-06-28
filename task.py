## Importing libraries and files
from crewai import Task

from agents import doctor, verifier, nutritionist, exercise_specialist
from tools import search_tool, BloodTestReportTool

## Creating a task to help solve user's query
help_patients = Task(
    description="Analyze the blood test report at {file_path} and provide a comprehensive medical analysis based on the user's query: {query}. "
    "Review all blood markers, identify any abnormalities, and provide evidence-based medical recommendations. "
    "Include normal ranges for key markers and explain the clinical significance of any deviations. "
    "Provide clear, actionable health advice while maintaining professional medical standards.",

    expected_output="""Provide a comprehensive blood test analysis including:
- Summary of key findings and overall health assessment
- Detailed analysis of each blood marker with normal ranges
- Identification of any abnormalities and their clinical significance
- Evidence-based medical recommendations and next steps
- Clear, professional language suitable for patient communication
- References to current medical guidelines where applicable""",

    agent=doctor,
    async_execution=False,
)

## Creating a nutrition analysis task
nutrition_analysis = Task(
    description="Analyze the blood test results at {file_path} to provide evidence-based nutritional recommendations. "
    "Focus on markers that indicate nutritional status such as vitamins, minerals, and metabolic indicators. "
    "Consider the user's query: {query} and provide personalized dietary guidance. "
    "Recommend appropriate foods, supplements if needed, and lifestyle modifications based on the blood work.",

    expected_output="""Provide comprehensive nutritional analysis including:
- Assessment of nutritional status based on blood markers
- Specific dietary recommendations with food examples
- Supplement recommendations if deficiencies are identified
- Meal planning suggestions and portion guidance
- Lifestyle modifications to support nutritional goals
- Evidence-based recommendations with scientific backing""",

    agent=nutritionist,
    async_execution=False,
)

## Creating an exercise planning task
exercise_planning = Task(
    description="Create a safe, personalized exercise plan based on the blood test results at {file_path} and health status. "
    "Consider markers that affect exercise capacity such as cardiovascular health, metabolic function, and inflammatory markers. "
    "Address the user's query: {query} and design an appropriate fitness program. "
    "Include safety considerations and progression guidelines.",

    expected_output="""Create a comprehensive exercise plan including:
- Assessment of current fitness level based on blood markers
- Safe exercise recommendations appropriate for health status
- Progressive workout plans with clear intensity guidelines
- Cardiovascular and strength training components
- Safety considerations and contraindications
- Monitoring and progression guidelines""",

    agent=exercise_specialist,
    async_execution=False,
)

## Creating a verification task
verification = Task(
    description="Verify that the uploaded document at {file_path} is a valid blood test report suitable for medical analysis. "
    "Check for the presence of essential blood markers, laboratory information, and proper formatting. "
    "Ensure the document contains sufficient information for meaningful analysis.",

    expected_output="""Provide verification results including:
- Confirmation of document type and validity
- Assessment of completeness and quality of blood test data
- Identification of key markers present in the report
- Recommendations for additional testing if needed
- Quality assessment of the laboratory report""",

    agent=verifier,
    async_execution=False
)