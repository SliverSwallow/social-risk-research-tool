from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet


def generate_pdf_report(filename, data, result):
    doc = SimpleDocTemplate(filename)
    styles = getSampleStyleSheet()

    content = []

    # Title
    content.append(Paragraph("SOCIAL RISK ASSESSMENT REPORT", styles["Title"]))
    content.append(Spacer(1, 12))

    # Context
    content.append(Paragraph("1. CONTEXT", styles["Heading2"]))
    content.append(Paragraph(
        "This report evaluates structural social risk based on housing, labor, demographic conditions, and welfare support.",
        styles["BodyText"]
    ))
    content.append(Spacer(1, 12))

    # Input
    content.append(Paragraph("2. INPUT INDICATORS", styles["Heading2"]))
    content.append(Paragraph(f"Housing Cost Ratio: {data['housing']}", styles["BodyText"]))
    content.append(Paragraph(f"Employment Stability: {data['employment']}", styles["BodyText"]))
    content.append(Paragraph(f"Fertility Rate: {data['fertility']}", styles["BodyText"]))
    content.append(Paragraph(f"Welfare Level: {data['welfare']}", styles["BodyText"]))
    content.append(Spacer(1, 12))

    # Risk
    content.append(Paragraph("3. RISK ASSESSMENT", styles["Heading2"]))
    content.append(Paragraph(f"Base Risk: {result['risk_score']}", styles["BodyText"]))
    content.append(Paragraph(f"Adjusted Risk: {result['adjusted_risk']}", styles["BodyText"]))
    content.append(Paragraph(f"Trust Score: {result['trust_score']}", styles["BodyText"]))
    content.append(Paragraph(f"Risk Level: {result['risk_level']}", styles["BodyText"]))
    content.append(Spacer(1, 12))

    # Issues
    content.append(Paragraph("4. KEY ISSUES", styles["Heading2"]))
    for issue in result["key_issues"]:
        content.append(Paragraph(f"- {issue}", styles["BodyText"]))
    content.append(Spacer(1, 12))

    # Interpretation
    content.append(Paragraph("5. INTERPRETATION", styles["Heading2"]))
    content.append(Paragraph("The results indicate that structural pressure remains significant, but welfare support partially mitigates its impact on households.",
                             styles["BodyText"]))
    content.append(Paragraph(result["interpretation"], styles["BodyText"]))
    
    content.append(Spacer(1, 12))

    # Policy
    content.append(Paragraph("6. POLICY FOCUS", styles["Heading2"]))
    for rec in result["recommended_focus"]:
        content.append(Paragraph(f"- {rec}", styles["BodyText"]))

    # Build PDF
    doc.build(content)

    return filename