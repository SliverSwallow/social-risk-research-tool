from fastapi import FastAPI
from app.schema import InputData, OutputData
from app.model import calculate_strain, apply_welfare, calculate_trust, classify_risk
from app.interpret import build_interpretation, policy_recommendation
from app.model_fuzzy import run_model
from reports.report_pdf import generate_pdf_report
from fastapi.responses import FileResponse


app = FastAPI(title="Social Risk Screening Tool")


@app.post("/analyze", response_model=OutputData)
def analyze(data: InputData):

    result = run_model(
        data.housing_cost_ratio,
        data.employment_stability,
        data.fertility_rate,
        data.welfare_level
    )

    return result

@app.post("/report/pdf")
def generate_pdf(data: InputData):

    result = run_model(
        data.housing_cost_ratio,
        data.employment_stability,
        data.fertility_rate,
        data.welfare_level
    )

    
    
    from datetime import datetime
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    file_path = f"outputs/report_{timestamp}.pdf"
    
    generate_pdf_report(
        file_path,
        {
            "housing": data.housing_cost_ratio,
            "employment": data.employment_stability,
            "fertility": data.fertility_rate,
            "welfare": data.welfare_level
        },
        result
    )

    return FileResponse(file_path, media_type='application/pdf', filename=file_path)