import java.security.Provider;
import java.security.Provider.Service;
import java.security.Security;
import sun.security.ec.SunEC;

public class ECCProviderTest {

    public static void main(final String[] args) {
        Provider sunEC = new SunEC();
        Security.addProvider(sunEC);
        for(Service service : sunEC.getServices()) {
            System.out.println(service.getType() + ": " 
                    + service.getAlgorithm());
        }
    }

}
