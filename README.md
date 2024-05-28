<center>
  <img src="https://github.com/mohammedshaneeb-ai/bucket/blob/main/Hire%20AI.png" alt="HireAI-logo" align="middle">
  <h2 style="text-align: center;"></h2>

</center>


# Hire AI

Hire AI is a machine learning-based project leveraging Large Language Models (LLMs) to assist both recruiters and job seekers. This project aims to streamline the hiring process by addressing several common challenges on both sides.

## The Problem

### For Job Seekers:
1. **Manual Data Entry**: Applicants often have to fill in details such as name, email, phone number, education, and skills manually, which is time-consuming.
2. **Resume Matching Uncertainty**: Job seekers often don't know how well their resume matches a job description, leading to the possibility of their resume not being shortlisted.
3. **Job Description Overload**: Reading and understanding long job descriptions can be time-consuming.

### For Recruiters:
1. **High Volume of Applicants**: Posting a job on a job portal can result in many applicants, making it difficult to read all resumes, shortlist candidates, and schedule interviews.
2. **Human Error**: Recruiters might miss out on good applicants due to the inability to thoroughly review all resumes, leading to potential human error.

## How Hire AI Solves These Problems

### For Job Seekers:
1. **Automated Data Extraction**: Hire AI extracts all relevant information such as name, email, phone number, education, and skills from the applicant's uploaded resume, reducing manual entry.
2. **Job Match Score**: Applicants can see how well their resume matches a job post, identify missing elements, and receive suggestions for improvement.
3. **Job Description Summary**: Hire AI provides a concise summary of the job description, saving applicants time.

### For Recruiters:
1. **Smart Shortlisting**: Recruiters can shortlist resumes using simple natural language prompts and questions related to job descriptions and applicant resumes. Examples of queries include:
    - Shortlist top applicants.
    - Shortlist top 2 applicants.
    - Shortlist applicants with a score above 80%.
    - Shortlist applicants with more than 2 years of experience.
    - Shortlist applicants with skills in prompt engineering.
    - Count the number of applicants.
2. **Comprehensive Screening**: The system thoroughly reviews all resumes, ensuring good applicants are not overlooked and reducing human error.

## Behind the Scene How Hire AI Works:

<table>
<h3>Applicant Side</h3>
  <tr>
    <td align="center">
      <h2>Resume Extraction</h2>
      <img src="https://github.com/mohammedshaneeb-ai/bucket/blob/main/hireai/workflow/Resume%20Extraction.png" alt="Paper 1" width="400">
    </td>
    <td align="center">
      <h2>Job Application Process</h2>
      <img src="https://github.com/mohammedshaneeb-ai/bucket/blob/main/hireai/workflow/Job%20Application%20Proces.png" alt="Paper 2" width="400">
    </td>
  </tr>
  <h3>Recruiter Side</h3>
  <tr>
    <td align="center">
      <h2>Job Post Process</h2>
      <img src="https://github.com/mohammedshaneeb-ai/bucket/blob/main/hireai/workflow/Save%20job%20post.png" alt="Paper 3" width="400">
    </td>
    <td align="center">
      <h2>Shortlisting</h2>
      <img src="https://github.com/mohammedshaneeb-ai/bucket/blob/main/hireai/workflow/Shortlisting.png" alt="Paper 4" width="400">
    </td>
  </tr>
</table>





## Installation

To install and set up Hire AI, follow these steps:

1. Clone the repository:
    ```bash
    git clone https://github.com/mohammedshaneeb-ai/HireAI.git
    ```
2. Navigate to the project directory:
    ```bash
    cd hireai
    ```
3. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```
4. Run the application:
    ```bash
    python manage.py runserver
    ```

## Usage

### For Job Seekers:
1. Upload your resume.
2. View your job match score and get suggestions for improvement.
3. Get a summary of job descriptions.

### For Recruiters:
1. Post job descriptions.
2. Use natural language prompts to shortlist candidates.
3. Review shortlisted candidates and schedule interviews.

## Contributing

We welcome contributions to Hire AI! Please follow these steps to contribute:

1. Fork the repository.
2. Create a new branch:
    ```bash
    git checkout -b feature/your-feature
    ```
3. Make your changes and commit them:
    ```bash
    git commit -m 'Add your feature'
    ```
4. Push to the branch:
    ```bash
    git push origin feature/your-feature
    ```
5. Create a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contact

For questions or feedback, please contact [shaneebkottakkal@gmail.com](mailto:shaneebkottakkal@gmail.com).

