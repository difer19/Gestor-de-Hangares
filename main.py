from launcher import Launcher

if __name__ == "__main__":
    Launchers = Launcher()
    lg = Launchers.iniciarLogin()
    if lg.afiliacion[0] == "Aeropuerto el campanero":
        Launchers.iniciarAdministrador()
    else:
        Launchers.iniciarFunAerolinea()