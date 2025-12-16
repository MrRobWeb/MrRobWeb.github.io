export const projects = [
  {
    title: 'Build and maintanance of a cloud framework',
    role: 'Senior Architect',
    industry: '',
    technologies: [
      'Python|JavaScript|Scala',
      'Terraform',
      'Docker',
      'Git',
      'AWS CloudFormation|CDK',
      'aws-sdk,boto3',
      'AWS Data Services: Glue,Athena,Kinesis,Step Functions,S3',
      'AWS DevOps Services: ECR,ECS,Codebuild,Codepipeline,Codecommit,SNS,CloudWatch,DynamoDB,EC2,Cloud9'
    ],
    date: 'April 2022 - Today',
    description: `As a Senior Architect I am responsible to establish and maintain a cloud framework for cloud pipelines. The aim of the framework is to create pipelines on a yaml or json based configuration structure. Those configs leverage and chain multiple cloud services into one consistent pipeline, for instance, you can chain the following kind of tasks: generative AI, data transformation, auditing, reporting, logging, validation, messaging, streaming and many more. Therefore, I build and train a global team of 10 engineers, including code reviews. Besides, a git branching strategy using semantic versioning for a two-weekly release cycle is introduced.`
  },
  {
    title: 'CI/CD Infrastructure for more then 100 deplyoments',
    role: 'Lead DevOps Engineer',
    industry: 'Energy Services',
    technologies: [
      'Terraform',
      'AWS Codebuild|Codepipeline|Codecommit|ECR|ECS',
      'Git',
      'CDK',
      'AWS CloudFormation',
      'Docker',
      'ECR'
    ],
    date: 'April 2022 - Today',
    description: `"Build once - deploy everywhere", according to this principle an innovative data migration solution was developed. For a large vendor in the energy service sector a new billing platform will be introduced. Therefore, more then 100 deployments of data migration pipelines are planned. To ensure deployment and removal of infrastructure for those migration activities, a CI/ CD process is developed using Terraform, Docker and AWS DevOps capabilites (Codebuild,Codepipeline,Codecommit, ECR, DynamoDB). Additionally, this CI/CD integration covers release updates from our cloud framework for those deployments.`
  },
  {
    title: 'Design, developement and architecture of a progressive webapp to configure data pipelines',
    role: 'Frontend Engineer',
    industry: 'Energy Services',
    technologies: ['Vite', 'Vue3', 'Tailwind CSS', 'aws-sdk', 'AWS DynamoDB', 'AWS App Runner'],
    date: 'April 2022 - Today',
    description: `For a large vendor in the energy service sector a new billing platform will be introduced. More then 100 legal entites will be onboarded to this new billing platform. Therefore, a data migration from the legacy ERP system (SAP IS-U) to this billing platform needs to be conducted. It is planned to prepare highly scalable but standardized migration pipelines, which can be configured. Therefore, I am designing and developing a progressive webapp, which is running on AWS App Runner using my favourite frontend tech stack, which consists of Vite, Vue3 and Tailwind. AWS is used as Cloud environment. For this reason I leverage the capabilites of DynamoDB as configuration data storage service. Therfore, aws-sdk is used to develope the webapp. `
  },
  {
    title: 'Developement & architecture of custom analytics webapps',
    role: 'Frontend Engineer | Lead Consultant',
    industry: 'Fincancial Services - Healthcare',
    technologies: [
      'Vite',
      'Vue3',
      'Tailwind CSS',
      'Javascript',
      'React',
      'Next JS',
      'Qlik APIs',
      'Power BI-REST-APIs'
    ],
    date: 'January 2017 - March 2022',
    description: `As analytics expert and frontend engineer you can leverage the strengths of web programming and the analytics engines of leading BI vendors like Qlik and Power BI. Both offer APIs to integrate already created analytics dashboard into customizable progressive web apps. This enables powerfull applications, where it is possible to design beautifull interactive dashboards with a unique analytics path for an astonishing end user experience.`
  },
  {
    title: 'Implementation of data analytics architecture for enterprise level reporting',
    role: 'Data Engineer | Lead Consultant',
    industry:
      'Manufacturing - Automotive - Fincancial Services - Healthcare - Insurance - Public Services - Energy Services',
    technologies: ['Qlik', 'Microsoft SSAS & SSIS', 'PowerBI', 'AWS', 'Python'],
    date: 'September 2014 - March 2022',
    description: `During my time as Data Engineer | Lead Consultant I was in charge of a full IT analytics architecture integration of a new BI software into the current IT landscape of the customer. This includes project management from the start as well as technical consulting such as the sizing of servers and installation of software, data extraction and connectivity provisioning of the BI software to ERP systems such as SAP, Microsoft Dynamics, and CRM systems like SalesForce. Usually, in colaboration with ERP & CRM consultants a data valuation was conducted and based on this data models, analytics reports and dashboards were designed - developed. Finally, a customized user administration process was implemented, which is especially important for highly sensitive data. `
  },
  {
    title: 'Trainings in data analytics and data engineering',
    role: 'Trainer',
    industry: 'Energy Services',
    technologies: ['Data Literacy', 'BI Design', 'Data Modelling', 'Data Transformation', 'Qlik Deep Dive'],
    date: 'September 2014 - March 2022',
    description: `As trainer I worked on the creation of several trainings in data analytics and data engineering area. This includes teaching general designing concepts to create beautiful dashboards, data modelling fundamentals as well as general data literacy topics. Additionally, I've designed deep dive trainings using advanced Qlik ETL techniques and Qlik Administration for a world wide audience.`
  }
];
