import java.io.IOException;
import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.SQLException;
import java.util.ArrayList;

public class TestSnowboard {

    public static void main(String args[]) throws SQLException {
        try{
        Connection conn = getConnection();
        MyQuery mquery = new MyQuery(conn);
        System.out.println(mquery);
        System.out.println("Connection Success!\n");
        } catch (SQLException e) {
            e.printStackTrace();
        }


        OptimalSpecs specs = new OptimalSpecs();

        Person person1 = new Person(69, 130, 0, false, true, 3, 400, 500);
        Snowboard recc = specs.getRec(person1);
    }

    public static Connection getConnection() throws SQLException {
        Connection connection;
        try {
            Class.forName("com.mysql.cj.jdbc.Driver");

        } catch (ClassNotFoundException e1) {
            e1.printStackTrace();
        }

        //Create a connection to the database
        String serverName = "localhost:3306";
        String mydatabase = "snowboarddb"; //change needed
        String url = "jdbc:mysql://" + serverName + "/" + mydatabase; // a JDBC url
        String username = "root"; //change needed
        String password = "Ny3xpg99100-"; //change needed

        connection = DriverManager.getConnection(url, username, password);
        return connection;
    }
}
