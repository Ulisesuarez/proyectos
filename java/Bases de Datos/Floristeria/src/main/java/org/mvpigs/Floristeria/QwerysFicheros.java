package org.mvpigs.Floristeria;

import java.io.BufferedWriter;
import java.io.FileWriter;
import java.io.IOException;
import java.io.PrintWriter;
import java.nio.charset.StandardCharsets;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.ResultSet;
import java.sql.ResultSetMetaData;
import java.sql.SQLException;
import java.sql.Statement;
import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

public class QwerysFicheros {
	private static String databaseName="PanelActividades";
	private static String connectionName="localhost:3306";

	public static void main(String[] args)
	{
		cargarQuerys();
			
	}

private static void cargarQuerys() {
	Connection conn = null;
	Statement stmt = null;
	ResultSet rs = null;
	List<String> lines=null;
	System.out.println("Introduce el path de tu archivo: ");
	Scanner input = new Scanner(System.in);
	String Path = input.nextLine();
	System.out.println(Path);

	try (Connection connection = DriverManager.getConnection("jdbc:mysql://"+connectionName+"/"+databaseName,"root","A203hora"))
	{
		try {
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

}}
	
/*	stmt.addBatch(linea.substring(0, linea.indexOf(";")));
			}
		}
		stmt.executeBatch();
		rs=stmt.getResultSet();
		int contador=0;*/

