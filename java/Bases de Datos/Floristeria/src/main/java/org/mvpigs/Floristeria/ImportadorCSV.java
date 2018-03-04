package org.mvpigs.Floristeria;
import java.io.FileReader;
import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.Statement;



public class ImportadorCSV {

	
	
	public static void main(String[] args)
	{
		readCsvUsingLoad();
			
	}


	private static void readCsvUsingLoad()
	{
		Connection conn = null;
	
	Statement stmt = null;

	ResultSet rs = null;
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

}
