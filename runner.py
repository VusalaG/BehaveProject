import os
import shutil


class BehaveTestRunner:
    def __init__(self, tags=None, feature_files=None):
        self.report_format = 'allure_behave.formatter:AllureFormatter'
        self.output_dir = 'allure-results'
        self.tags = tags if tags else []
        self.feature_files = feature_files if feature_files else []

    def run_tests(self):
        # Clear allure-results directory
        shutil.rmtree(self.output_dir, ignore_errors=True)
        command = f'behave -f {self.report_format} -o {self.output_dir}'
        if self.tags:
            command += ' ' + ' '.join([f'--tags="{tag}"' for tag in self.tags])

        command += ' ' + ' '.join(self.feature_files)

        os.system(command)

    def generate_allure_report(self):
        os.system(f'allure generate --clean -o allure-report {self.output_dir}')


    def open_generated_allure_report(self):
        os.system(f'allure open allure-report')


if __name__ == '__main__':
    tags = ['@smoke1']
    feature_files = ['features']
    runner = BehaveTestRunner(tags=tags, feature_files=feature_files)
    runner.run_tests()
    runner.generate_allure_report()
    runner.open_generated_allure_report()


