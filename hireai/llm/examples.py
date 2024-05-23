examples = [
    {"input": "from job_id=19. List all applicants.", "query": "SELECT * FROM adminapp_jobapplication WHERE job_id = 19;"},
    {
        "input": "from job_id=19. Shortlist top applicants ",
        "query": "SELECT * FROM adminapp_jobapplication WHERE job_id = 19 ORDER BY score DESC LIMIT 3;",
    },
    {
        "input": "from job_id=23. Shortlist top 5 applicants",
        "query": "SELECT * FROM adminapp_jobapplication WHERE job_id = 23 ORDER BY score DESC LIMIT 5;",
    },
    {
        "input": "from job_id=14. Shortlist 5 applicants",
        "query": "SELECT * FROM adminapp_jobapplication WHERE job_id = 14 ORDER BY score DESC LIMIT 5;",
    },
    {
        "input": "from job_id=18. Shortlist applicants with score more than 80",
        "query": "SELECT * FROM adminapp_jobapplication WHERE job_id = 18 AND score > 80;",
    },
    {
        "input": "from job_id=18. Shortlist applicants with skills Lora and Fine-Tuning",
        "query": "SELECT * FROM adminapp_jobapplication WHERE (LOWER(skills) LIKE '%lora%' OR LOWER(skills) LIKE '%fine%tuning%') AND job_id = 18;",
    },
    {
        "input": "from job_id=17. Shortlist applicants with skills Transformers",
        "query": "SELECT * FROM adminapp_jobapplication WHERE (LOWER(skills) LIKE '%transformers%') AND job_id = 17;",
    },
    {
        "input": "from job_id=24. Shortlist applicants with score more than 75",
        "query": "SELECT * FROM adminapp_jobapplication WHERE job_id = 24 AND score > 75;",
    },
    {
        "input": "from job_id=24. Shortlist applicants with experience more than 2 years",
        "query": "SELECT * FROM adminapp_jobapplication WHERE job_id = 24 AND experience > 2;",
    },
    {
        "input": "from job_id=11. Shortlist applicants with experience more than 3 years",
        "query": "SELECT * FROM adminapp_jobapplication WHERE job_id = 11 AND experience > 3;",
    },
    {
        "input": "from job_id=23.How many are applied?",
        "query": 'SELECT COUNT(*) AS total_applications FROM adminapp_jobapplication WHERE job_id = 23;',
    },
]