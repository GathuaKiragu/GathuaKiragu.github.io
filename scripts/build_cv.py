"""Build the public CV. Requires reportlab; run from the repository root."""
from pathlib import Path
from reportlab.platypus import SimpleDocTemplate, Paragraph, PageBreak
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib import colors
from reportlab.lib.pagesizes import A4

OUT = Path('assets/Brian_Gathua_CV.pdf')
styles = getSampleStyleSheet()
for name,size,leading,color in [('Body',10.5,15,'#29313B'),('Section',12,16,'#172B43'),('Role',11,15,'#172B43'),('Small',9,13,'#465362')]:
 styles.add(ParagraphStyle(name=name,fontName='Helvetica',fontSize=size,leading=leading,textColor=colors.HexColor(color),spaceAfter=7))
styles['Section'].fontName='Helvetica-Bold';styles['Section'].spaceBefore=13;styles['Section'].keepWithNext=True
styles['Role'].fontName='Helvetica-Bold';styles['Role'].spaceBefore=6;styles['Role'].keepWithNext=True
styles.add(ParagraphStyle(name='Name',fontName='Helvetica-Bold',fontSize=23,leading=28,spaceAfter=7))
styles.add(ParagraphStyle(name='Subtitle',fontName='Helvetica',fontSize=12,leading=17,spaceAfter=10,textColor=colors.HexColor('#172B43')))
story=[]
def p(text,style='Body'):story.append(Paragraph(text,styles[style]))
def bullet(text):
 story.append(Paragraph('- '+text,ParagraphStyle('BulletCV',parent=styles['Body'],leftIndent=9,firstLineIndent=-9,spaceAfter=5)))
def heading(text):p(text,'Section')
def role(company,title,dates):
 p(company+' | '+title,'Role');p(dates,'Small')

p('Brian Gathua Kiragu','Name')
p('Engineering Lead &amp; Senior Software Engineer','Subtitle')
p('Nairobi, Kenya | EAT (UTC+3) | Remote roles and long-term contracts','Small')
p('<link href="mailto:kiragugathua@gmail.com">kiragugathua@gmail.com</link> | +254 701 250 543','Small')
p('<link href="https://gathuakiragu.github.io">gathuakiragu.github.io</link> | <link href="https://github.com/GathuaKiragu">github.com/GathuaKiragu</link>','Small')
p('<link href="https://linkedin.com/in/kiragu-gathua-138b97122/">linkedin.com/in/kiragu-gathua-138b97122</link>','Small')
heading('Professional summary')
p('Software engineer and hands-on engineering lead building mobile applications and backend systems for energy distribution, delivery, and insurance. Lead five engineers at Jaguar Petroleum, contributing to system design, development, hiring, and code reviews. Designed cylinder tracking workflows supporting 10,000+ cylinders across four depots and reworked data handling for a 1,000-sensor BLE pilot. Run Funmo, an independent web development agency.')
heading('Professional experience')
role('Jaguar Petroleum Limited','Engineering Lead','April 2024 - Present')
bullet('Lead five engineers across mobile, backend, IoT, and infrastructure; contribute directly to architecture, implementation, code reviews, hiring, and Git-based delivery.')
bullet('Architected LPG cylinder lifecycle workflows covering onboarding, warehouse movements, dispatch, refilling, delivery personnel, and customer allocation; platform supports 10,000+ cylinders across four depots.')
bullet('Delivered Flutter and backend capabilities for JGas and fleet/mobility workflows, connecting mobile applications with operational services and enterprise systems.')
bullet('Investigated elevated MySQL load in a 1,000-sensor BLE pilot; introduced Redis caching and reduced the frequency of persisted updates to manage database writes. Performance improvement has not yet been measured.')
bullet('Contributed to the migration from NetSuite to ERPNext to reduce vendor dependency and improve access to implementation resources.')
role('ICEA LION Group','Full Stack Developer','April 2022 - April 2025')
bullet('Developed and maintained customer and agent-facing insurance applications with a reported combined user base of more than 1,000.')
bullet('Implemented Flutter mobile features and REST API integrations for insurance workflows and enterprise backend services; collaborated with product and engineering on debugging and delivery.')
role('Upande Limited','Technology leadership and Android development','2017 - April 2022')
bullet('Joined as an intern and progressed into Android development and technology leadership responsibilities.')
bullet('Contributed to environmental monitoring software and related digital solutions.')

story.append(PageBreak())
heading('Selected project work')
p('JGas and LPG cylinder tracking','Role')
p('Designed cylinder lifecycle workflows and delivered Flutter and backend capabilities for LPG operations. The tracking platform supports 10,000+ cylinders across four depots. JGas has a reported 500+ users; the measurement period is to be confirmed.')
p('IoT monitoring','Role')
p('Investigated database workload during a pilot involving 1,000 BLE sensors. Introduced Redis caching and reduced persisted sensor update frequency to manage high-frequency MySQL writes. This is pilot scale; no measured performance gain is claimed.')
p('ICEA LION Agents and customer applications','Role')
p('Developed and maintained Flutter features and REST integrations supporting customer and agent insurance workflows. The reported 1,000+ users cover both applications combined.')
p('JMobility','Role')
p('Delivered Flutter and backend capabilities for fleet and last-mile delivery workflows, integrating operational services. Work focused on connecting mobile delivery activity with backend operations.')
heading('Independent web development')
p('Funmo | <link href="https://funmo.africa">funmo.africa</link>','Role')
p('Run a web development agency alongside engineering work, building websites for clients. Security is a priority in the approach to software: limiting access, protecting sensitive data, and reviewing what an application exposes.')
heading('Technical skills')
p('<b>Mobile:</b> Flutter, Dart, Android (Java/Kotlin), Redux, BLoC/Cubit, Riverpod, Provider.<br/><b>Backend and data:</b> Java, Spring Boot, Node.js, REST APIs, PostgreSQL, MySQL, Redis, WebSockets.<br/><b>Infrastructure and delivery:</b> Linux, Docker, Git, CI/CD, Nginx, cloud deployments.<br/><b>Systems:</b> Architecture, ERP integrations, IoT data pipelines, payment APIs.')
heading('Leadership and collaboration')
p('Lead a five-person engineering team; have mentored and trained 20+ developers. Experience in technical interviews, hiring, code reviews, architecture decisions, and discussions with nontechnical stakeholders.')
heading('Education and training')
p('<b>Diploma in Information Technology</b><br/>Jomo Kenyatta University of Agriculture and Technology (JKUAT)')
p('<b>Software Engineering Certificate</b><br/>Moringa School')

def footer(canvas,doc):
 canvas.saveState();canvas.setFont('Helvetica',8);canvas.setFillColor(colors.HexColor('#627080'))
 canvas.drawString(44,27,'Brian Gathua Kiragu');canvas.drawRightString(A4[0]-44,27,str(doc.page));canvas.restoreState()
SimpleDocTemplate(str(OUT),pagesize=A4,rightMargin=44,leftMargin=44,topMargin=38,bottomMargin=42,title='Brian Gathua Kiragu - CV',author='Brian Gathua Kiragu').build(story,onFirstPage=footer,onLaterPages=footer)
print(OUT)
