import java.util.ArrayList;
import java.util.List;

public class Snowboard {
    String name;
    String manu;
    double price;
    int length, year;
    boolean isCamber;
    boolean isDirectional;
    boolean isWide;


    public Snowboard(String name, String manu, double price,int length, boolean isCamber, boolean isDirectional, int year, boolean isWide){
        this.name = name;
        this.manu = manu;
        this.price = price;
        this.length = length;
        this.isCamber = isCamber;
        this.isDirectional = isDirectional;
        this.year = year;
        this.isWide = isWide;
    }

    @Override
    public String toString(){
        return "Name:" + this.name + "\nManufacturer: " + this.manu + "\nLength: " + this.length + "\nIs Camber? " + this.isCamber +  "\nPrice: " + this.price;
    }
}
