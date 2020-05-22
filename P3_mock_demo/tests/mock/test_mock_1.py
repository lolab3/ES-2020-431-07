from unittest.mock import patch
from unittest import mock
from P3_mock_demo.src import Travel
@mock.patch('src.Bank')
class Test1:
    def Test_PagoV1(self, mock_bank):
        v1 = Travel.Flight.Flight(1234567, 'Barcelona', 35, 4)
        v2 = Travel.Flight.Flight(3215674, 'Madrid', 40, 3)
        v = []
        v.append(v1)
        v.append(v2)
        f = Travel.Flights.Flights(v)
        d1 = Travel.Destination.Destination('Barcelona', 5)
        d2 = Travel.Destination.Destination('Madrid', 4)
        r = []
        r.append(d1)
        r.append(d2)
        D = Travel.Destinations.Destinations(r)
        V = Travel.Travel(f, D, 123)
        V.Pago_viaje('MASTERCARD', 'joan', 42122343, 872)

Test1.Test_PagoV1(Test1)



