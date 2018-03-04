package org.mvpigs.Floristeria;
import java.io.BufferedWriter;
import java.io.FileWriter;
import java.io.IOException;
import java.io.PrintWriter;
import java.nio.charset.StandardCharsets;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.sql.Connection;
import java.sql.DatabaseMetaData;
import java.sql.DriverManager;
import java.sql.ResultSetMetaData;
import java.sql.SQLException;
import java.sql.Statement;
import java.sql.ResultSet;
import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;
/**
 * Hello world!
 *
 */
public class Floristeria 
{
	private static String databaseName="PanelActividades";
	private static String connectionName="localhost:3306";


    public static void main( String[] args )
    {
    	Connection conn = null;
    	
		Statement stmt = null;

		ResultSet rs = null;
    	
    	try {
    	    conn =  DriverManager.getConnection("jdbc:mysql://localhost:3306/","root","A203hora");
			String PanelActividades= "use PanelActividades";
			stmt = conn.createStatement();
			stmt.execute(PanelActividades);
    	    DatabaseMetaData dbmd = conn.getMetaData();
    	    
    	    ResultSet catalogos = dbmd.getCatalogs();
    	    
    	     
    	    while (catalogos.next())
    	    {	
    	        System.out.println(catalogos.getString(1));
    	    }
    	    stmt = conn.createStatement();



		    if (stmt.execute("DESC Avatar")) {

		        rs = stmt.getResultSet();

		        while (rs.next()) {

		            String Host = rs.getString(1);

		            

		            System.out.println(Host + "\t" );

		        }

		    }
    	    QueryConsola();
    	    
    	}catch (SQLException ex) {
    	    // handle any errors
    	    System.out.println("SQLException: " + ex.getMessage());
    	    System.out.println("SQLState: " + ex.getSQLState());
    	    System.out.println("VendorError: " + ex.getErrorCode());
    		}
    	
    }




    public static void QueryConsola(){
    	try (Connection connection = DriverManager.getConnection("jdbc:mysql://"+connectionName+"/"+databaseName,"root","A203hora"))
    	{
    	Statement stmt = null;
    	ResultSet rs = null;
    	
    	System.out.println("Que acción quieres hacer? \n1 Modificar datos \n2 Introducir datos \n3 Borrar Datos \n4 Escribir la orden ");
    	
    	Scanner input = new Scanner(System.in);
    	int elegido=esNumero(input,6);
    	String orden="";
    	switch (elegido){
    		
    	    		
    	case 1: Update();
    	
    	case 2: Insert();
    		
    	case 3: Delete();
    		
    	case 4: System.out.println("Escribe la orden:");stmt=connection.createStatement();
    			input = new Scanner(System.in);
    			orden=input.nextLine();
				if (!orden.isEmpty()){
						System.out.println(orden);
					
							stmt.execute(orden);
							rs=stmt.getResultSet();
    		
				}
    	}
    	} catch (SQLException e) {
			
			e.printStackTrace();
		}
    	}			
		private static void Delete() {
		// TODO Auto-generated method stub
		
	}




		private static void Insert() {
		
		
			Connection conn = null;
			Statement stmt = null;
			ResultSet rs = null;
			String queryParteColumnas="";
			int indiceTabla=1;
			String Tabla="";
			String queryparteValores="";
			
			
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
				System.out.println("Introduce el número  de la Tabla en la que deseas insertar datos: ");
				Scanner input = new Scanner(System.in);
				
				indiceTabla = esNumero(input,Tablas.length+1);
				
				if (indiceTabla<=Tablas.length){System.out.println(Tablas[indiceTabla]);
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
				
				System.out.println("En cuantas columnas deseas añadir datos? (1-"+String.valueOf(Columnas.size())+")");
				
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
				queryparteValores="( ";
				System.out.println("Cuantas filas quieres introducir");
				input = new Scanner(System.in);
				int NFilas=esNumero(input,1000);
				System.out.println("introcude los valores separados por comas: 'ej:valor1, valor2'");
				if (NFilas==1){
					
					
					input = new Scanner(System.in);
					queryparteValores=queryparteValores+input.nextLine()+" )";
					
				}
				for (int i=0; i<NFilas;i++){
					if(i<NFilas-1) {
						System.out.println("Fila "+String.valueOf(i)+":");
						input = new Scanner(System.in);
						queryparteValores=queryparteValores+input.nextLine()+" ), ( ";
					}
					else{
						System.out.println("Fila "+String.valueOf(i)+":");
						input = new Scanner(System.in);
						queryparteValores=queryparteValores+input.nextLine()+" )";
					}
				}
				
				}
				
				
				
				String loadQuery = "INSERT INTO "+Tabla+" ( "+queryParteColumnas+") VALUES "+queryparteValores;
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




		private static void Update() {
			Connection conn = null;
			Statement stmt = null;
			ResultSet rs = null;
			String queryParteColumnas="";
			int indiceTabla=1;
			String Tabla="";
			String queryparteValores="";
			
			
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
				System.out.println("Introduce el número  de la Tabla en la que deseas insertar datos: ");
				Scanner input = new Scanner(System.in);
				
				indiceTabla = esNumero(input,Tablas.length+1);
				
				if (indiceTabla<=Tablas.length){System.out.println(Tablas[indiceTabla]);
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
				
				System.out.println("En cuantas columnas deseas añadir datos? (1-"+String.valueOf(Columnas.size())+")");
				
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
				queryparteValores="( ";
				System.out.println("Cuantas filas quieres introducir");
				input = new Scanner(System.in);
				int NFilas=esNumero(input,1000);
				System.out.println("introcude los valores separados por comas: 'ej:valor1, valor2'");
				if (NFilas==1){
					
					
					input = new Scanner(System.in);
					queryparteValores=queryparteValores+input.nextLine()+" )";
					
				}
				for (int i=0; i<NFilas;i++){
					if(i<NFilas-1) {
						System.out.println("Fila "+String.valueOf(i)+":");
						input = new Scanner(System.in);
						queryparteValores=queryparteValores+input.nextLine()+" ), ( ";
					}
					else{
						System.out.println("Fila "+String.valueOf(i)+":");
						input = new Scanner(System.in);
						queryparteValores=queryparteValores+input.nextLine()+" )";
					}
				}
				
				}
				
				
				
				String loadQuery = "INSERT INTO "+Tabla+" ( "+queryParteColumnas+") VALUES "+queryparteValores;
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




		static int esNumero(Scanner input,int rango){
					boolean esNumero=false;
					while (esNumero==false){
						try{
							String Strinput=input.nextLine();
							if (Integer.parseInt(Strinput)<rango+1){
							return Integer.parseInt(Strinput);	
							}
							else{throw new NumberFormatException();}
						
							
						}
						catch (NumberFormatException nfe){
							System.out.println("Solo puedes introducir números del 1 al "+String.valueOf(rango));
							System.out.println("Introduce el número: ");
							input = new Scanner(System.in);
						}
					}
				
				return 0;}
			
}
    	
    	/* 	try {
    			lines = Files.readAllLines(Paths.get(Path), StandardCharsets.UTF_8);
    			System.out.println(lines.get(1));
    			
    		} catch (IOException e) {
    			
    			e.printStackTrace();
    		}
    		for (String linea : lines){
    			stmt=connection.createStatement();
    			if (!linea.isEmpty()){
    			System.out.println(linea.substring(0, linea.indexOf(";")));
    						
    			stmt.execute(linea.substring(0, linea.indexOf(";")));
    			rs=stmt.getResultSet();
    			try(FileWriter fw = new FileWriter("HistorialConsultas.txt", true);
    				    BufferedWriter bw = new BufferedWriter(fw);
    				    PrintWriter out = new PrintWriter(bw))
    				{
    				 out.println("\n"+linea+"\n");
    				 
    				 
    				 ResultSetMetaData metadata = rs.getMetaData();
    				 int columnCount = metadata.getColumnCount();    
    				 for (int i = 1; i <= columnCount; i++) {
    				        out.print(metadata.getColumnName(i) + ",\t");      
    				    }
    				out.println("\n");
    				 while (rs.next()) {
    				        String row = "";
    				        for (int i = 1; i <= columnCount; i++) {
    				            row += rs.getString(i) + ",\t";          
    				        }
    				        out.println(row);

    				    }
    				
    				} catch (IOException e) {
    				    //exception handling left as an exercise for the reader
    				}
    			}
    		}
    		
    		
    	} catch (SQLException e) {
    		// TODO Auto-generated catch block
    		e.printStackTrace();
    	}

    }
	 
    
 }

    	      
    	     
    	    
    	    // Do something with the Connection

    	  
    	} 
    	}
    	
    	
    	// assume that conn is an already created JDBC connection (see previous examples)

    	Statement stmt = null;
    	ResultSet rs = null;

    	try {
    	    stmt = conn.createStatement();
    	    rs = stmt.executeQuery("SELECT foo FROM bar");

    	    // or alternatively, if you don't know ahead of time that
    	    // the query will be a SELECT...

    	    if (stmt.execute("SELECT foo FROM bar")) {
    	        rs = stmt.getResultSet();
    	    }

    	    // Now do something with the ResultSet ....
    	}
    	catch (SQLException ex){
    	    // handle any errors
    	    System.out.println("SQLException: " + ex.getMessage());
    	    System.out.println("SQLState: " + ex.getSQLState());
    	    System.out.println("VendorError: " + ex.getErrorCode());
    	}
    	finally {
    	    // it is a good idea to release
    	    // resources in a finally{} block
    	    // in reverse-order of their creation
    	    // if they are no-longer needed

    	    if (rs != null) {
    	        try {
    	            rs.close();
    	        } catch (SQLException sqlEx) { } // ignore

    	        rs = null;
    	    }

    	    if (stmt != null) {
    	        try {
    	            stmt.close();
    	        } catch (SQLException sqlEx) { } // ignore

    	        stmt = null;
    	    }
    	}
        System.out.println( "Hello World!" );
    }
*/
    	    
