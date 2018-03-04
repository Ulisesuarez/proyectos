package org.mvpigs.Floristeria;

import java.io.FileReader;
import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.Statement;
import java.util.ArrayList;
import java.util.Scanner;

public class ImportCsV {
		private static String databaseName="PanelActividades";
		private static String connectionName="localhost:3306";

		public static void main(String[] args)
		{
			readCsv();
				
		}


		private static void readCsv()
		{
		Connection conn = null;
		Statement stmt = null;
		ResultSet rs = null;
		String queryParteColumnas="";
		System.out.println("Introduce el path de tu archivo: ");
		Scanner input = new Scanner(System.in);
		String Path = input.nextLine();
		System.out.println(Path);
		int indiceTabla=1;
		String Tabla="";
		
		
		try (Connection connection = DriverManager.getConnection("jdbc:mysql://"+connectionName+"/"+databaseName,"root","A203hora"))
		{
			stmt = connection.createStatement();
			stmt.execute("SHOW TABLES;");
			rs=stmt.getResultSet();
			String[] Tablas=new String[13];
			int contador=0;
			while (rs.next()) {
				contador++;
					
		            String Host = rs.getString(1);
		            
					Tablas[contador]=rs.getString(1);
		            System.out.println( String.valueOf(contador) + "\t"+Tablas[contador] );
			}
			System.out.println("Introduce el número  de la Tabla: ");
			input = new Scanner(System.in);
			boolean esNumero=false;
			while (esNumero==false){
				try{
					indiceTabla = Integer.parseInt(input.nextLine());
					esNumero=true;
				}
				catch (NumberFormatException nfe){
					System.out.println("Solo puedes introducir números del 1 al "+String.valueOf(Tablas.length));
					System.out.println("Introduce el número  de la Tabla: ");
					input = new Scanner(System.in);
				}
			}
			
			if (indiceTabla<Tablas.length){System.out.println(Tablas[indiceTabla]);
			String loadQuery="DESC "+Tablas[indiceTabla];
			Tabla=Tablas[indiceTabla];
			stmt = connection.createStatement();
			stmt.execute(loadQuery);
			rs=stmt.getResultSet();
			contador=0;
			ArrayList<String> Columnas= new ArrayList<String>();
			
			while (rs.next()) {
				
					
		            String Columna = rs.getString(1);
		            
					Columnas.add(Columna);
		            System.out.println( String.valueOf(contador)+"\t" + Columnas.get(contador) );
		            contador++;
			}
			
			System.out.println("Cuantas columnas deseas añadir (1-"+String.valueOf(Columnas.size())+")");
			
			input = new Scanner(System.in);
			int NColumn=esNumero(input,Columnas.size());
			
			if (NColumn==1){
				
				System.out.print("¿Cuál? (0-"+String.valueOf(Columnas.size()-1)+")");
				input = new Scanner(System.in);
				queryParteColumnas=queryParteColumnas+Columnas.get(esNumero(input,Columnas.size()-1));
				
			}
			for (int i=0; i<NColumn;i++){
				if(i<NColumn-1) {
					System.out.println("Ordenalas, Cual va? (0-"+String.valueOf(Columnas.size()-1)+")");
					input = new Scanner(System.in);
					queryParteColumnas=queryParteColumnas+Columnas.get(esNumero(input,Columnas.size()-1))+", ";
				}
				else{
					System.out.println("Ordenalas, Cual va? (0-"+String.valueOf(Columnas.size()-1)+")");
					input = new Scanner(System.in);
					queryParteColumnas=queryParteColumnas+Columnas.get(esNumero(input,Columnas.size()-1));
				}
			}
			
			System.out.println("LOAD DATA LOCAL INFILE '" + Path + "' INTO TABLE Productos( "+queryParteColumnas+") ");
			}
			
			
			String loadQuery = "LOAD DATA LOCAL INFILE '" + Path + "' INTO TABLE "+Tabla+" FIELDS TERMINATED BY ',' LINES TERMINATED BY '\\n' ( "+queryParteColumnas+")";
			stmt = connection.createStatement();
			stmt.execute(loadQuery);
			
			Statement stmt2 = connection.createStatement();
			stmt2.execute("SELECT "+queryParteColumnas+" FROM "+Tabla);
			 rs = stmt2.getResultSet();

		        while (rs.next()) {

		            String Host = rs.getString(1);

		            

		            System.out.println(Host + "\t" );

		        }
			
			
			rs.close();
		    stmt.close();
		}catch (Exception e)
		{
			e.printStackTrace();
	}
		}
		
		
		private static int esNumero(Scanner input,int rango){
			boolean esNumero=false;
			while (esNumero==false){
				try{
					
				
					return Integer.parseInt(input.nextLine());
				}
				catch (NumberFormatException nfe){
					System.out.println("Solo puedes introducir números del 1 al "+String.valueOf(rango));
					System.out.println("Introduce el número: ");
					input = new Scanner(System.in);
				}
			}
		
		return 0;}
	}

/*		
		
			try (Connection connection = DriverManager.getConnection("jdbc:mysql://localhost:3306/Floristeria","root","A203hora"))
			{

					String loadQuery = "LOAD DATA LOCAL INFILE '" + "/home/ulises/Micarpeta/proyectos/java/Bases de Datos/Floristeria/src/main/java/org/mvpigs/Floristeria/DataProductoNombre.csv" + "' INTO TABLE Productos( Nombre) ";
					System.out.println(loadQuery);
					stmt = connection.createStatement();
					stmt.execute(loadQuery);
					Statement stmt2 = connection.createStatement();
					stmt2.execute("SELECT Nombre FROM Productos");
					 rs = stmt2.getResultSet();

				        while (rs.next()) {

				            String Host = rs.getString(1);

				            

				            System.out.println(Host + "\t" );

				        }
			}
			catch (Exception e)
			{
					e.printStackTrace();
			}
			System.out.println("FIN");
		}

	}*/
