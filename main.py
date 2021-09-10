from launcher import Launcher

if __name__ == "__main__":
    Launchers = Launcher()
    lg = Launchers.iniciarLogin()
    if lg.afiliacion[0] == "aeropuerto el campanero":
        Launchers.iniciarAdministrador()
    else:
        Launchers.iniciarFunAerolinea(lg.afiliacion[0])
 


