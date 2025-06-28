# Blood Test Analyzer - AI-Powered Medical Report Analysis

A professional blood test analysis system built with CrewAI that provides comprehensive medical insights, nutritional recommendations, and exercise planning based on blood test reports.

---

## ⚠️ Important Notice

- **Web search and advanced CrewAI tools are currently disabled** due to the `crewai_tools` dependency not being installed (Windows build issues with `chroma-hnswlib`).
- **Core features (PDF analysis, medical/nutrition/exercise agents) work fully.**
- If you want web search or advanced CrewAI tools, see the troubleshooting section for installation help.

---

## 🐛 Bugs Found and Fixed

### Critical Bugs Fixed:

1. **Missing LLM Configuration** 
   - **Bug**: `llm = llm` in `agents.py` was undefined
   - **Fix**: Added proper OpenAI LLM configuration with environment variable support

2. **Missing Dependencies**
   - **Bug**: Missing imports for `PDFLoader`, `langchain_openai`, and other required packages
   - **Fix**: Added all missing dependencies to `requirements.txt` and proper imports

3. **Incorrect Tool Method Definitions**
   - **Bug**: `read_data_tool` was defined as async but called synchronously
   - **Fix**: Changed to synchronous method and added proper error handling

4. **File Path Handling Issues**
   - **Bug**: `run_crew` function ignored the provided `file_path` parameter
   - **Fix**: Updated function to properly use the uploaded file path

5. **Unprofessional Agent Descriptions**
   - **Bug**: Agents had unprofessional, potentially harmful descriptions
   - **Fix**: Rewritten all agents with professional, evidence-based medical expertise

6. **Missing Error Handling**
   - **Bug**: Limited error handling for file operations and API calls
   - **Fix**: Added comprehensive error handling and validation

7. **Incorrect Task Configuration**
   - **Bug**: Tasks referenced undefined agents and had unprofessional descriptions
   - **Fix**: Updated all tasks with proper agent references and professional descriptions

8. **Missing File Type Validation**
   - **Bug**: No validation for uploaded file types
   - **Fix**: Added PDF file type validation

---

## 🚀 Features (Working Now)

- **Comprehensive Blood Test Analysis**: Professional medical interpretation of blood markers
- **Nutritional Recommendations**: Evidence-based dietary guidance based on blood results
- **Exercise Planning**: Safe, personalized fitness recommendations
- **Document Verification**: Validation of uploaded medical reports
- **RESTful API**: Easy integration with web and mobile applications
- **Professional Medical Standards**: All recommendations follow evidence-based medical guidelines

---

## 🛠️ Setup Instructions

### Prerequisites
- Python 3.10, 3.11, or 3.12 (CrewAI does not support Python 3.14+)
- OpenAI API key

### Installation

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd blood-test-analyser-debug
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up environment variables**
   ```bash
   # Copy the example environment file
   cp env_example.txt .env
   # Edit .env and add your API keys
   OPENAI_API_KEY=your_openai_api_key_here
   ```

4. **Run the application**
   ```bash
   python main.py
   ```

The API will be available at `http://localhost:8000`

---

## 📚 API Documentation

### Endpoints

#### GET `/`
Health check endpoint
```bash
curl http://localhost:8000/
```

#### POST `/analyze`
Analyze a blood test report

**Parameters:**
- `file` (required): PDF file containing blood test report
- `query` (optional): Specific question or analysis request (default: "Summarise my Blood Test Report")

**Example Request:**
```bash
curl -X POST "http://localhost:8000/analyze" \
  -H "Content-Type: multipart/form-data" \
  -F "file=@path/to/your/blood_test.pdf" \
  -F "query=Analyze my cholesterol levels and provide recommendations"
```

**Example Response:**
```json
{
  "status": "success",
  "query": "Analyze my cholesterol levels and provide recommendations",
  "analysis": "Comprehensive blood test analysis...",
  "file_processed": "blood_test.pdf"
}
```

### Error Responses

- `400 Bad Request`: Invalid file type or missing file
- `500 Internal Server Error`: Processing error or API configuration issues

---

## 🏗️ Architecture

### Components

1. **Agents** (`agents.py`)
   - **Doctor**: Primary medical analyst for blood test interpretation
   - **Verifier**: Validates uploaded documents
   - **Nutritionist**: Provides dietary recommendations
   - **Exercise Specialist**: Creates fitness plans

2. **Tools** (`tools.py`)
   - **BloodTestReportTool**: PDF reading and processing
   - **NutritionTool**: Nutritional analysis (future enhancement)
   - **ExerciseTool**: Exercise planning (future enhancement)

3. **Tasks** (`task.py`)
   - **help_patients**: Main analysis task
   - **nutrition_analysis**: Nutritional guidance task
   - **exercise_planning**: Fitness planning task
   - **verification**: Document validation task

4. **API** (`main.py`)
   - FastAPI server with file upload and analysis endpoints

---

## 🔧 Configuration

### Environment Variables

| Variable | Description | Required |
|----------|-------------|----------|
| `OPENAI_API_KEY` | OpenAI API key for LLM access | Yes |

### Model Configuration

The system uses GPT-3.5-turbo by default. To change the model, modify the `llm` configuration in `agents.py`:

```python
llm = ChatOpenAI(
    model="gpt-4",  # Change model here
    temperature=0.7,
    api_key=os.getenv("OPENAI_API_KEY")
)
```

---

## 🧪 Testing

### Manual Testing

1. **Start the server**
   ```bash
   python main.py
   ```

2. **Test with sample PDF**
   - Use the provided `data/sample.pdf` or upload your own blood test report
   - Test different queries to verify analysis quality

3. **Test error handling**
   - Try uploading non-PDF files
   - Test with invalid API keys
   - Test with corrupted PDF files

---

## 🔮 Future Enhancements

### Planned Features (Not Yet Available)

1. **Queue Worker Model**
   - Redis/Celery integration for concurrent request handling
   - Background job processing
   - Job status tracking

2. **Database Integration**
   - PostgreSQL/MongoDB for storing analysis results
   - User management and authentication
   - Historical analysis tracking

3. **Web Search & Advanced CrewAI Tools**
   - Requires successful installation of `crewai_tools` and dependencies
   - See troubleshooting below for help

---

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

---

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

---

## ⚠️ Disclaimer

This system provides AI-powered analysis and recommendations but should not replace professional medical advice. Always consult with qualified healthcare providers for medical decisions.

---

## 🆘 Support & Troubleshooting

For issues and questions:
1. Check the troubleshooting section below
2. Review the API documentation
3. Open an issue on GitHub

### Common Issues

1. **"OpenAI API key not found"**
   - Ensure your `.env` file exists and contains a valid `OPENAI_API_KEY`

2. **"PDF reading error"**
   - Verify the PDF file is not corrupted
   - Ensure the file contains readable text (not just images)

3. **"Analysis timeout"**
   - Check your OpenAI API quota
   - Verify internet connectivity

4. **"Import errors"**
   - Run `pip install -r requirements.txt` to install all dependencies
   - Ensure you're using Python 3.10, 3.11, or 3.12

5. **"Cannot install crewai_tools or chroma-hnswlib"**
   - On Windows, ensure you have [Visual Studio Build Tools](https://visualstudio.microsoft.com/visual-cpp-build-tools/) with the "Desktop development with C++" workload
   - Restart your computer after installation
   - Try installing with:
     ```bash
     pip install crewai-tools
     ```
   - If it still fails, core features will work, but web search and advanced tools will be unavailable

---
