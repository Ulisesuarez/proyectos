package org.ubsrf.TSPcaseData;

public class CityData {

    private static Integer [][] distanciaCiudades= {{0,25,52,25,23},
                                                    {25,0,13,15,45},
                                                    {52,13,0,15,27},
                                                    {25,15,15,0,32},
                                                    {23,45,27,32,0}};



    public static Integer[][] getDistanciaCiudades() {
        return distanciaCiudades;
    }
}


