from launcher import Launcher


if __name__ == "__main__":
    Launchers = Launcher()
    lg = Launchers.iniciarLogin()
    print(lg)
    Launchers.iniciarAdministrador()
    # Launchers.iniciarFunAerolinea()