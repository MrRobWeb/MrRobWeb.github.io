export const toolStacks = [
  {
    title: 'Cloud',
    subTitle: 'Leveraging IT services in the cloud',
    icon: 'fa-solid fa-cloud',
    description: `Cloud engineering simply excites me!`,
    skills: {
      programmingLanguages: {
        description: `I've been working with the following Cloud Providers:`,
        values: [
          { name: 'AWS', skillValue: '0.8' },
          { name: 'Azure', skillValue: '0.3' },
          { name: 'GCP', skillValue: '0.2' }
        ]
      },
      frameworks: {
        description: `I've been working with the following cloud services:`,
        values: [
          { name: 'Spark | AWS Glue', skillValue: '0.95' },
          { name: 'Presto | AWS Athena', skillValue: '0.95' },
          { name: 'AWS S3 | DynamoDB', skillValue: '0.95' },
          { name: 'AWS Step Functions', skillValue: '0.95' },
          { name: 'AWS Quicksight', skillValue: '0.85' },
          { name: 'AWS Kinesis', skillValue: '0.8' },
          { name: 'AWS Redshift', skillValue: '0.7' },
          { name: 'Microsoft Analysis Services | Power BI', skillValue: '0.7' }
        ]
      },
      libraries: {
        description: `These are noteworthy additional cloud skills:`,
        values: [
          { name: 'boto3', skillValue: '0.95' },
          { name: 'awswrangler', skillValue: '0.95' },
          { name: 'linux', skillValue: '0.9' },
          { name: 'terraform', skillValue: '0.9' },
          { name: 'Docker', skillValue: '0.8' }
        ]
      }
    }
  },
  {
    title: 'Data Engineering | Data Analytics | Machine Learning',
    subTitle: 'The art of getting insights from data.',
    icon: 'fa-solid fa-chart-column',
    description: `Being a data magician in the first place, I've been working in this area since finishing my studies.`,
    skills: {
      programmingLanguages: {
        description: `In the data world, programming languages are your hammer and chissel to form your data. For this reason these skills are essential:`,
        values: [
          { name: 'Python', skillValue: '0.95' },
          { name: 'SQL', skillValue: '0.95' },
          { name: 'Scala', skillValue: '0.5' },
          { name: 'Qlik ETL', skillValue: '0.98' },
          { name: 'Java', skillValue: '0.7' },
          { name: 'SAP ABAB', skillValue: '0.6' }
        ]
      },
      frameworks: {
        description: `I've been working with the following tools and frameworks:`,
        values: [
          { name: 'Spark | AWS Glue', skillValue: '0.9' },
          { name: 'Presto | AWS Athena', skillValue: '0.95' },
          { name: 'Kafka', skillValue: '0.5' },
          { name: 'Qlik', skillValue: '0.95' },
          { name: 'Power BI', skillValue: '0.9' }
        ]
      },
      libraries: {
        description: `These are noteworthy libraries:`,
        values: [
          { name: 'Pandas', skillValue: '0.95' },
          { name: 'scikit-learn', skillValue: '0.65' },
          { name: 'tensorflow', skillValue: '0.4' },
          { name: 'boto3', skillValue: '0.95' },
          { name: 'awswrangler', skillValue: '0.95' }
        ]
      }
    }
  },
  {
    title: 'Frontend',
    subTitle: 'Generate user friendly interaction between human and machines.',
    icon: 'fa-solid fa-image',
    description: `Creating a user friendly UI in data analytics is key. Foremost, it's important that every user interpretates the depicted data in the same way. Nothing is worse then creating discussion in the analytics world.`,
    skills: {
      programmingLanguages: {
        description: `Programming languages I've been using:`,
        values: [
          { name: 'Javascript', skillValue: '0.93' },
          { name: 'Typescript', skillValue: '0.9' },
          { name: 'Dart', skillValue: '0.5' },
          { name: 'HTML', skillValue: '0.75' },
          { name: 'CSS', skillValue: '0.7' }
        ]
      },
      frameworks: {
        description: `Even, my favourite frontend setup consists of Vue 3, Tailwind CSS created with Vite and Pinia as statemanagement library, I took a plunge into several other frameworks and libraries:`,
        values: [
          { name: 'Vue.js|Pinia', skillValue: '0.95' },
          { name: 'Vite', skillValue: '0.8' },
          { name: 'Angular', skillValue: '0.4' },
          { name: 'Flutter', skillValue: '0.5' },
          { name: 'Tailwind CSS', skillValue: '0.9' }
        ]
      },
      libraries: {
        description: `Noteworthy libraries:`,
        values: [
          { name: 'Babylon JS', skillValue: '0.75' },
          { name: 'React|Redux|Vite', skillValue: '0.65' },
          { name: 'Chart JS', skillValue: '0.8' },
          { name: 'aws-sdk', skillValue: '0.7' },
          { name: 'webpack', skillValue: '0.7' }
        ]
      }
    }
  },
  {
    title: 'Backend',
    subTitle: 'The fundament of every great application.',
    icon: 'fa-solid fa-server',
    description: `My experience regarding backend technologies is project sufficient. I've been working on building REST APIs using Node.js, Flask/Django and Spring. Nevertheless, I am still growing expertise in this field.`,
    skills: {
      programmingLanguages: {
        description: `Programming languages:`,
        values: [
          { name: 'Python', skillValue: '0.94' },
          { name: 'Javascript', skillValue: '0.93' },
          { name: 'Java|Maven', skillValue: '0.6' }
        ]
      },
      frameworks: {
        description: `Frameworks I took a plunge into:`,
        values: [
          { name: 'Node', skillValue: '0.85' },
          { name: 'Flask', skillValue: '0.5' },
          { name: 'Django', skillValue: '0.5' },
          { name: 'Spring | Spring Boot', skillValue: '0.5' }
        ]
      },
      libraries: {
        description: `Noteworthy tools & libraries:`,
        values: [
          { name: 'Express JS', skillValue: '0.8' },
          { name: 'Postman', skillValue: '0.7' }
        ]
      }
    }
  },
  {
    title: 'DevOps',
    subTitle: 'The philosophy to automate the integration of great devolopment work into operation.',
    icon: 'fa-solid fa-gears',
    description: `In my opinion DevOps is not about coding, it's about knowing your business & IT operation, defining a release and update process and then building the analogue CI/CD structure as well as version management, which fits your needs.`,
    skills: {
      programmingLanguages: {
        description: `Essential tools & programming languages:`,
        values: [
          { name: 'Python', skillValue: '0.94' },
          { name: 'Javascript', skillValue: '0.93' },
          { name: 'Git', skillValue: '0.9' },
          { name: 'Bash | Shell', skillValue: '0.9' },
          { name: 'Docker', skillValue: '0.8' },
          { name: 'Docker Compose', skillValue: '0.7' },
          { name: 'Kubernetes', skillValue: '0.5' }
        ]
      },
      frameworks: {
        description: `Cloud Environments:`,
        values: [
          { name: 'AWS - Codepipeline | Codebuild | Codecommit', skillValue: '0.95' },
          { name: 'Azure DevOps', skillValue: '0.6' }
        ]
      },
      libraries: {
        description: `Additional tools and knwowledge:`,
        values: [
          { name: 'Linux', skillValue: '0.9' },
          { name: 'Node.js', skillValue: '0.85' },
          { name: 'Networks', skillValue: '0.85' },
          { name: 'Postman', skillValue: '0.7' },
          { name: 'IAM management', skillValue: '0.95' }
        ]
      }
    }
  }
];
