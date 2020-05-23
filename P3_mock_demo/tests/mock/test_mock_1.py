from P3_mock_demo.src import Bank
from P3_mock_demo.src import Flight
from P3_mock_demo.src import Destination
from P3_mock_demo.src import Travel
from P3_mock_demo.src import Flights
from P3_mock_demo.src import Destinations
from P3_mock_demo.src import PaymentData
from P3_mock_demo.src import User
from P3_mock_demo.src import Cars
from P3_mock_demo.src import Hotel
from P3_mock_demo.src import Hotels
from P3_mock_demo.src import ListCars
from P3_mock_demo.src import Traveller
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
        hotels = [Hotel.Hotel('L2310', 'Don Candido', 3, 1, 5, 120), Hotel.Hotel('M1291', 'Vela', 2, 1, 7, 2000)]
        h = Hotels.Hotels(hotels)
        coches = [Cars.Cars('6677TZ', 'Renault', 'Terrassa', 10, 100), Cars.Cars('1238TL', 'Opel', 'Barcelona', 5, 60)]
        c = ListCars.Car(coches)
        Tv = Traveller.Traveller(' ', 0)
        # datos de pago
        Pd = PaymentData.PaymentData()
        Pd.solicitarDatos('MASTERCARD', 'denis', 42122343, 872)
        B = Bank.Bank()

        # datos de usuario
        Usuario = User.User('denis', '32421213', 'hernan cortes, n 24', '651097675', 'denismontoyadelcanto@gmail.com')
        # Usuario.set_user('denis', '32421213', 'hernan cortes, n 24', '651097675', 'denismontoyadelcanto@gmail.com')
        V = Travel.Travel(f, D, 123, Usuario, Pd, c, h, 1, Tv)
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
        hotels = [Hotel.Hotel('L2310', 'Don Candido', 3, 1, 5, 120), Hotel.Hotel('M1291', 'Vela', 2, 1, 7, 2000)]
        h = Hotels.Hotels(hotels)
        coches = [Cars.Cars('6677TZ', 'Renault', 'Terrassa', 10, 100), Cars.Cars('1238TL', 'Opel', 'Barcelona', 5, 60)]
        c = ListCars.Car(coches)
        Tv = Traveller.Traveller(' ', 0)
        # datos de pago
        Pd = PaymentData.PaymentData()
        Pd.solicitarDatos('MASTERCARD', 'denis', 42122343, 872)
        # datos de usuario
        Usuario = User.User('denis', '32421213', 'hernan cortes, n 24', '651097675', 'denismontoyadelcanto@gmail.com')
        # Usuario.set_user('denis', '32421213', 'hernan cortes, n 24', '651097675', 'denismontoyadelcanto@gmail.com')
        V = Travel.Travel(f, D, 123, Usuario, Pd, c, h , 1 , Tv)
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
        hotels = [Hotel.Hotel('L2310', 'Don Candido', 3, 1, 5, 120), Hotel.Hotel('M1291', 'Vela', 2, 1, 7, 2000)]
        h = Hotels.Hotels(hotels)
        coches = [Cars.Cars('6677TZ', 'Renault', 'Terrassa', 10, 100), Cars.Cars('1238TL', 'Opel', 'Barcelona', 5, 60)]
        c = ListCars.Car(coches)
        Tv = Traveller.Traveller(' ', 0)
        # datos de pago
        Pd = PaymentData.PaymentData()
        Pd.solicitarDatos('MASTERCARD', 'denis', 42122343, 872)
        # datos de usuario
        Usuario = User.User('denis', '32421213', 'hernan cortes, n 24', '651097675', 'denismontoyadelcanto@gmail.com')
        # Usuario.set_user('denis', '32421213', 'hernan cortes, n 24', '651097675', 'denismontoyadelcanto@gmail.com')
        V = Travel.Travel(f, D, 123, Usuario, Pd, c, h , 1 , Tv)
        result = V.confirmar_reserva_vuelos(mock_Skyscanner)
        self.assertFalse(result)

    @mock.patch('P3_mock_demo.src.Rentalcars')
    def test_ReservaCocheV1(self, mock_Rentalcars):
        mock_Rentalcars.confirm_reserve.return_value = False
        v = [Flight.Flight(1234567, 'Barcelona', 35, 4), Flight.Flight(3215674, 'Madrid', 40, 3)]
        f = Flights.Flights(v)
        r = [Destination.Destination('Barcelona', 5), Destination.Destination('Madrid', 4)]
        D = Destinations.Destinations(r)
        hotels = [Hotel.Hotel('L2310', 'Don Candido', 3, 1, 5, 120), Hotel.Hotel('M1291', 'Vela', 2, 1, 7, 2000)]
        h = Hotels.Hotels(hotels)
        coches = [Cars.Cars('6677TZ', 'Renault', 'Terrassa', 10, 100), Cars.Cars('1238TL', 'Opel', 'Barcelona', 5, 60)]
        c = ListCars.Car(coches)
        Tv = Traveller.Traveller(' ', 0)
        c = ListCars.Car(coches)
        # datos de pago
        Pd = PaymentData.PaymentData()
        Pd.solicitarDatos('MASTERCARD', 'denis', 42122343, 872)
        # datos de usuario
        Usuario = User.User('denis', '32421213', 'hernan cortes, n 24', '651097675', 'denismontoyadelcanto@gmail.com')
        V = Travel.Travel(f, D, 123, Usuario, Pd, c, h , 1 , Tv)
        result = V.confirmar_reserva_vehiculos(mock_Rentalcars)
        self.assertFalse(result)

    @mock.patch('P3_mock_demo.src.Booking')
    def test_ReservaHotelV1(self, mock_Booking):
        mock_Booking.confirm_reserve.return_value = False
        # datos de hotel
        v = [Flight.Flight(1234567, 'Barcelona', 35, 4), Flight.Flight(3215674, 'Madrid', 40, 3)]
        f = Flights.Flights(v)
        r = [Destination.Destination('Barcelona', 5), Destination.Destination('Madrid', 4)]
        D = Destinations.Destinations(r)
        hotels = [Hotel.Hotel('L2310', 'Don Candido', 3, 1, 5, 120), Hotel.Hotel('M1291', 'Vela', 2, 1, 7, 2000)]
        h = Hotels.Hotels(hotels)
        coches = [Cars.Cars('6677TZ', 'Renault', 'Terrassa', 10, 100), Cars.Cars('1238TL', 'Opel', 'Barcelona', 5, 60)]
        c = ListCars.Car(coches)
        Tv = Traveller.Traveller(' ', 0)
        c = ListCars.Car(coches)
        # datos de pago
        Pd = PaymentData.PaymentData()
        Pd.solicitarDatos('MASTERCARD', 'denis', 42122343, 872)
        # datos de usuario
        Usuario = User.User('denis', '32421213', 'hernan cortes, n 24', '651097675', 'denismontoyadelcanto@gmail.com')
        V = Travel.Travel(f, D, 123, Usuario, Pd, c, h , 1 , Tv)
        result = V.confirmar_reserva_hoteles(mock_Booking)
        self.assertFalse(result)


    @mock.patch('P3_mock_demo.src.SkyScanner', 'P3_mock_demo.src.RentalCars' ,'P3_mock_demo.src.Booking')
    def test_ReservaTotal(self, mock_SkyScanner, mock_RentalCars, mock_Booking):
        mock_Booking.confirm_reserve.return_value = False
        # datos de hotel
        v = [Flight.Flight(1234567, 'Barcelona', 35, 4), Flight.Flight(3215674, 'Madrid', 40, 3)]
        f = Flights.Flights(v)
        r = [Destination.Destination('Barcelona', 5), Destination.Destination('Madrid', 4)]
        D = Destinations.Destinations(r)
        hotels = [Hotel.Hotel('L2310', 'Don Candido', 3, 1, 5, 120), Hotel.Hotel('M1291', 'Vela', 2, 1, 7, 2000)]
        h = Hotels.Hotels(hotels)
        coches = [Cars.Cars('6677TZ', 'Renault', 'Terrassa', 10, 100), Cars.Cars('1238TL', 'Opel', 'Barcelona', 5, 60)]
        c = ListCars.Car(coches)
        Tv = Traveller.Traveller(' ', 0)
        c = ListCars.Car(coches)
        # datos de pago
        Pd = PaymentData.PaymentData()
        Pd.solicitarDatos('MASTERCARD', 'denis', 42122343, 872)
        # datos de usuario
        Usuario = User.User('denis', '32421213', 'hernan cortes, n 24', '651097675', 'denismontoyadelcanto@gmail.com')
        V = Travel.Travel(f, D, 123, Usuario, Pd, c, h , 1 , Tv)
        result = V.confirmar_reserva_hoteles(mock_Booking)
        self.assertFalse(result)



if __name__ == '__main__':
    unittest.main()
