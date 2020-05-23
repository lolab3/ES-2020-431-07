from P3_mock_demo.src import Bank
from P3_mock_demo.src import Flight
from P3_mock_demo.src import Destination
from P3_mock_demo.src import Travel
from P3_mock_demo.src import Flights
from P3_mock_demo.src import Destinations
from P3_mock_demo.src import PaymentData
from P3_mock_demo.src import User
from P3_mock_demo.src import Booking
from P3_mock_demo.src import Rentalcars



import unittest
from unittest import mock


class TestV1(unittest.TestCase):

    def test_PagoV1(self):
        # datos de vuelos, destinos
        v = [Flight.Flight(1234567, 'Barcelona', 35, 4), Flight.Flight(3215674, 'Madrid', 40, 3)]
        f = Flights.Flights(v)
        r = [Destination.Destination('Barcelona', 5), Destination.Destination('Madrid', 4)]
        D = Destinations.Destinations(r)
        # datos de pago
        Pd = PaymentData.PaymentData()
        Pd.solicitarDatos('MASTERCARD', 'denis', 42122343, 872)
        B = Bank.Bank()
        # datos de usuario
        Usuario = User.User('denis', '32421213', 'hernan cortes, n 24', '651097675', 'denismontoyadelcanto@gmail.com')
        # Usuario.set_user('denis', '32421213', 'hernan cortes, n 24', '651097675', 'denismontoyadelcanto@gmail.com')
        V = Travel.Travel(f, D, 123, Usuario, Pd)
        result = V.Pago_viaje(B)
        self.assertTrue(result)

    @mock.patch('P3_mock_demo.src.Bank')
    def test_PagoV2(self, mock_bank):
        mock_bank.do_payment.return_value = False
        # datos de vuelos, destinos
        v = [Flight.Flight(1234567, 'Barcelona', 35, 4), Flight.Flight(3215674, 'Madrid', 40, 3)]
        f = Flights.Flights(v)
        r = [Destination.Destination('Barcelona', 5), Destination.Destination('Madrid', 4)]
        D = Destinations.Destinations(r)
        # datos de pago
        Pd = PaymentData.PaymentData()
        Pd.solicitarDatos('MASTERCARD', 'denis', 42122343, 872)
        # datos de usuario
        Usuario = User.User('denis', '32421213', 'hernan cortes, n 24', '651097675', 'denismontoyadelcanto@gmail.com')
        # Usuario.set_user('denis', '32421213', 'hernan cortes, n 24', '651097675', 'denismontoyadelcanto@gmail.com')
        V = Travel.Travel(f, D, 123, Usuario, Pd)
        result = V.Pago_viaje(mock_bank)
        self.assertFalse(result)

    @mock.patch('P3_mock_demo.src.Skyscanner')
    def test_PagoV3(self, mock_Skyscanner):
        mock_Skyscanner.confirm_reserve.return_value = False
        # datos de vuelos, destinos
        v = [Flight.Flight(1234567, 'Barcelona', 35, 4), Flight.Flight(3215674, 'Madrid', 40, 3)]
        f = Flights.Flights(v)
        r = [Destination.Destination('Barcelona', 5), Destination.Destination('Madrid', 4)]
        D = Destinations.Destinations(r)
        # datos de pago
        Pd = PaymentData.PaymentData()
        Pd.solicitarDatos('MASTERCARD', 'denis', 42122343, 872)
        # datos de usuario
        Usuario = User.User('denis', '32421213', 'hernan cortes, n 24', '651097675', 'denismontoyadelcanto@gmail.com')
        # Usuario.set_user('denis', '32421213', 'hernan cortes, n 24', '651097675', 'denismontoyadelcanto@gmail.com')
        V = Travel.Travel(f, D, 123, Usuario, Pd)
        result = V.confirmar_reserva(mock_Skyscanner)
        self.assertFalse(result)


if __name__ == '__main__':
    unittest.main()
