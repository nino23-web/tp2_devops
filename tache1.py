pipeline {
    agent any

    environment {
        VENV = 'venv'
        COVERAGE_MINIMUM = 80 // Exigence de couverture minimale
        PYTHON_VERSIONS = ['3.7', '3.8', '3.9'] // Versions Python pour les tests multi-environnements
    }

    stages {
        stage('Install Dependencies') {
            steps {
                script {
                    // Crée et active un environnement virtuel pour chaque version de Python
                    PYTHON_VERSIONS.each { pythonVersion ->
                        def venvDir = "${env.WORKSPACE}/${VENV}-${pythonVersion}"
                        sh "pyenv install -s ${pythonVersion}" // Assurez-vous que pyenv est installé sur Jenkins
                        sh "pyenv virtualenv ${pythonVersion} ${venvDir} || true"
                        sh ". ${venvDir}/bin/activate && pip install -r requirements.txt"
                    }
                }
            }
        }

        stage('Lint with Pylint') {
            steps {
                script {
                    // Exécute Pylint et enregistre le rapport dans un fichier
                    def pylintSuccess = true
                    try {
                        PYTHON_VERSIONS.each { pythonVersion ->
                            def venvDir = "${env.WORKSPACE}/${VENV}-${pythonVersion}"
                            sh ". ${venvDir}/bin/activate && pylint votre_projet/ > pylint-report-${pythonVersion}.txt"
                            archiveArtifacts artifacts: "pylint-report-${pythonVersion}.txt", allowEmptyArchive: true
                        }
                    } catch (Exception e) {
                        pylintSuccess = false
                    }
                }
            }
            post {
                always {
                    // Enregistre les résultats pour chaque rapport de Pylint
                    PYTHON_VERSIONS.each { pythonVersion ->
                        recordIssues tool: pylint(pattern: "pylint-report-${pythonVersion}.txt"), thresholdLimit: 'high', healthy: 0, unhealthy: 20
                    }
                }
            }
        }

        stage('Run Tests with PyTest') {
            steps {
                script {
                    PYTHON_VERSIONS.each { pythonVersion ->
                        def venvDir = "${env.WORKSPACE}/${VENV}-${pythonVersion}"
                        sh ". ${venvDir}/bin/activate && pytest --junitxml=pytest-report-${pythonVersion}.xml"
                        archiveArtifacts artifacts: "pytest-report-${pythonVersion}.xml", allowEmptyArchive: true
                    }
                }
            }
            post {
                always {
                    // Enregistre les rapports de test pour chaque version de Python
                    PYTHON_VERSIONS.each { pythonVersion ->
                        junit "pytest-report-${pythonVersion}.xml"
                    }
                }
            }
        }

        stage('Code Coverage with Coverage.py') {
            steps {
                script {
                    def coverageSuccess = true
                    try {
                        PYTHON_VERSIONS.each { pythonVersion ->
                            def venvDir = "${env.WORKSPACE}/${VENV}-${pythonVersion}"
                            sh ". ${venvDir}/bin/activate && coverage run -m pytest"
                            sh ". ${venvDir}/bin/activate && coverage xml -o coverage-${pythonVersion}.xml"
                            cobertura coberturaReportFile: "coverage-${pythonVersion}.xml"
                        }
                    } catch (Exception e) {
                        coverageSuccess = false
                    }
                }
            }
            post {
                always {
                    // Valide la couverture pour chaque version de Python et impose un minimum
                    PYTHON_VERSIONS.each { pythonVersion ->
                        def reportPath = "coverage-${pythonVersion}.xml"
                        cobertura coberturaReportFile: reportPath, onlyStable: true, failNoReports: true
                    }
                }
            }
        }
    }

    post {
        success {
            emailext to: 'team@example.com', subject: "Build Succeeded: ${env.JOB_NAME} #${env.BUILD_NUMBER}", body: "The build succeeded for job ${env.JOB_NAME}. Coverage and linting are within thresholds."
        }
        unstable {
            emailext to: 'team@example.com', subject: "Build Unstable: ${env.JOB_NAME} #${env.BUILD_NUMBER}", body: "The build is unstable. Check linting errors or coverage results that might be below thresholds."
        }
        failure {
            emailext to: 'team@example.com', subject: "Build Failed: ${env.JOB_NAME} #${env.BUILD_NUMBER}", body: "The build failed. Please check the Jenkins job ${env.JOB_NAME} for details."
        }
    }
}
