import java.net.DatagramSocket;
import java.net.InetAddress;
import java.net.DatagramPacket;

public class DatagramClient
{
    private final static String hostname ="180.123.139.174";
    private final static int port = 8887 ;
    private final static InetAddress host = InetAddress.getByName( hostname ) ;
    private final static name = "XHC#3";

    public static void main( String args[] )
    {
        double X=117.14112364303995;
        double Y=34.210311754345234;
        send(X,Y);
    }

    public static void send(double X,double Y)
    {
        DatagramSocket socket = null ;
        try
            {
                socket = new DatagramSocket() ;
                // Construct the datagram packet
                String msg = name + "," + String.valueOf(X) + "," + String.valueOf(Y) + ",,,,";
                byte [] data = msg.getBytes() ;
                DatagramPacket packet = new DatagramPacket( data, data.length, host, port ) ;

                // Send it
                socket.send( packet ) ;
            }
        catch( Exception e )
            {
                System.out.println( e ) ;
            }
        finally
            {
                if( socket != null )
                    socket.close() ;
            }

    }
}
