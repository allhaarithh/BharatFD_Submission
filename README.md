# BharatFD_Submission


## Setup
1. Clone repository
2. Create virtual environment
3. Install dependencies: `pip install -r requirements.txt`
4. Run migrations: `python manage.py migrate`
5. Start server: `python manage.py runserver`

## API Endpoints
- `/api/faqs/`: List all FAQs
- `/api/faqs/?lang=hi`: Get FAQs in Hindi
- `/api/faqs/?lang=bn`: Get FAQs in Bengali

## Running Tests
`pytest`