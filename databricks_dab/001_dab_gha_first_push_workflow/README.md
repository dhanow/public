# CI/CD workflow with DAB and GitHub Actions

NOTE: 
1. THIS NEEDS TO BE RUN FROM PUBLIC REPO, as environments can be created only in PUBLIC or paid repos
2. The action.yml must be created at the repo root i.e public/.github/workflows/action.yml
3. If your workflow keeps triggering pages-build-deployment workflow, then disable it by going to settings->pages and under "Branch" select "None" and save

You can use GitHub Actions along with Databricks CLI bundle commands to automate, customize, and run your CI/CD workflows from within your GitHub repositories

STEPS:
1. You can add GitHub Actions YAML files such as the following to your repo’s .github/workflows directory
2. Create an enviroment //you can only create environments for public repos, github pro and github team
   Go to GitHub
   Settings
   Environments
   New environment
   Give it a name "dev"

   Next 
   add a secret to the environment
   This is databricks pat token
   



refer:
* https://learn.microsoft.com/en-us/azure/databricks/dev-tools/bundles/ci-cd-bundles