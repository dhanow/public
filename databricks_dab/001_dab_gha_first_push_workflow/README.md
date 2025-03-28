# CI/CD workflow with DAB and GitHub Actions

#### Note:
1. THIS NEEDS TO BE RUN FROM PUBLIC REPO, as environments can be created only in PUBLIC or paid repos
2. The `action.yml` must be created at the repo root for example in my `public` repo under `.github/workflows/action.yml`

#### Few issues and fixes:
1. If your workflow keeps triggering pages-build-deployment workflow, then disable it by going to settings->pages and under "Branch" select "None" and save


#### STEPS
1. You can add GitHub Actions YAML files such as the following to your repo’s .github/workflows directory
2. Create an enviroment //you can only create environments for public repos, github pro and github team
   Go to GitHub
   Settings
   Environments
   New environment
   Give it a name "dev"

   Next 
   add a secret to the environment, in this example I have used PAT_TOKEN
   Set the variable PAT_TOKEN to a databricks pat token
   Use the variable PAT_TOKEN in your `action.yml`

#### IDE
* us vscode
* Install the Extensions for `github actions` and `databricks cli`
   * on the left blade you will find extensions, select the extension and click install

#### References
* https://learn.microsoft.com/en-us/azure/databricks/dev-tools/bundles/ci-cd-bundles

#### Help
* In github, go to the `actions.yml` and select edit. 
   * On the right side you will see `market place` and `documentation`
   * Use `documentation` to find help with yaml
   * use `market place` to find help with `actions`
* You can view the actions workflow in github
   * select `Actions` `All workflows` on the left navigation blade and you will see a list of workflow runs
   * Click on the latest run
      * you will see the jobs, you can click on a specific job to see the details
* You can click on `Deployments`
   * Select the `environment` and see the workflow runs associated with each environment
   * Click on `manage environment` and you can make changes to the environment. Same thing can be done from the `settings` too

      

