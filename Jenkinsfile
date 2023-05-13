pipeline {
    agent any

    stages {
        stage('Prepare workspace') {
            steps {
                sh """
                    ls
                    python3 --version
                    python3 -m venv venv
                    ls
                    . venv/bin/activate
                    python3 -m pip install pip-tools
                    pip-sync requirements.txt
                """
            }
        }

		stage('Update Steam') {
			steps {
				withCredentials([
					usernameColonPassword(credentialsId: 'steam_pass', variable: 'STEAM_USERPASS'),
					string(credentialsId: 'steam_2fa_secret', variable: 'FA_SECRET')
				]) {
					sh """
						. venv/bin/activate
						python3 -m steam_server_manager install-steam
					"""
				}
			}
		}

		stage('Install Arma3Server') {
			steps {
				withCredentials([
					usernameColonPassword(credentialsId: 'steam_pass', variable: 'STEAM_USERPASS'),
					string(credentialsId: 'steam_2fa_secret', variable: 'FA_SECRET')
				]) {
					sh """
						. venv/bin/activate
						python3 -m steam_server_manager install-arma-3-server
					"""
				}
			}
		}

		stage('Install Arma3 Mods') {
			steps {
				withCredentials([
					usernameColonPassword(credentialsId: 'steam_pass', variable: 'STEAM_USERPASS'),
					string(credentialsId: 'steam_2fa_secret', variable: 'FA_SECRET')
				]) {
					sh """
						. venv/bin/activate
						python3 -m steam_server_manager install-arma-3-mods
					"""
				}
			}
		}

		stage('Prepare bash file') {
			steps {
				sh """
					. venv/bin/activate
					python3 -m steam_server_manager prepare-bash-file
				"""
			}
		}

    }
}
