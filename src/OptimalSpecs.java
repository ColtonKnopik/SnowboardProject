import java.util.ArrayList;

public class OptimalSpecs {

    double targetLengthLow, targetLengthHigh;
    boolean width;

    public Snowboard getRec(Person person){
        targetLengthLow = calculateLength(person.height) - 2;
        targetLengthHigh = calculateLength(person.height) + 2;
        width = needsWide(person.weight, person.height);
        

        System.out.println(toString());
        return null;
    }

    public double calculateLength(int height){
        return height  * 2.54 * .9;
    }

    @Override
    public String toString(){
        return "Targeted Length Between " + targetLengthLow + " and " + targetLengthHigh +
                "\nNeeds a wide board? " + width;
    }

    public boolean needsWide(int weight, int height){

        double kiloWeight = weight / 2.205;
        double metersHeight = height / 39.37;
        double BMI = kiloWeight / (metersHeight * 2);
        if (BMI > 25)
            return true;

        else return false;
    }


    public void snowboardMatch(Person person, Snowboard snowboard){
        double matchQuotient = 0;

    }
}


