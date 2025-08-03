"""
Sensor interface for hardware sensor integration in sim-physics-engine.

This module provides the foundation for integrating hardware sensors with the physics
simulation engine. The SensorInterface class defines the contract that all sensor
implementations must follow, enabling consistent sensor data acquisition and integration
with the simulation loop.

The interface supports various types of sensors (accelerometers, gyroscopes, pressure
sensors, etc.) that can provide real-world data to enhance or validate simulation results.
"""

from abc import ABC, abstractmethod
from typing import Any, Dict, Optional, Union


class SensorInterface(ABC):
    """Abstract base class for hardware sensor integration.
    
    This interface defines the standard methods that all sensor implementations
    must provide to integrate with the physics simulation engine. Concrete sensor
    classes should inherit from this interface and implement all abstract methods.
    
    The interface supports the full sensor lifecycle from initialization through
    data acquisition to cleanup, ensuring consistent behavior across different
    sensor types and hardware platforms.
    """

    @abstractmethod
    def initialize_sensor(self, config: Optional[Dict[str, Any]] = None) -> bool:
        """Initialize the sensor hardware and establish communication.
        
        This method handles the setup and configuration of the sensor hardware,
        including establishing communication protocols, setting sampling rates,
        calibrating the sensor, and verifying proper operation.
        
        Args:
            config: Optional dictionary containing sensor-specific configuration
                parameters such as sampling rate, communication settings, calibration
                values, or other hardware-specific options. If None, default
                configuration will be used.
        
        Returns:
            bool: True if sensor initialization was successful, False otherwise.
            
        Raises:
            SensorError: If sensor hardware cannot be accessed or configured.
            ConnectionError: If communication with the sensor cannot be established.
        """
        pass

    @abstractmethod
    def read_data(self) -> Dict[str, Union[float, int, bool]]:
        """Read current sensor data and return formatted measurements.
        
        This method performs a single reading from the sensor hardware and returns
        the data in a standardized format. The returned dictionary should contain
        all relevant measurements with descriptive keys and appropriate data types.
        
        Returns:
            Dict[str, Union[float, int, bool]]: Dictionary containing sensor measurements
                with keys describing the measurement type (e.g., 'acceleration_x',
                'temperature', 'pressure') and values as the measured data. Units
                should be SI standard where applicable.
                
        Raises:
            SensorError: If sensor reading fails or returns invalid data.
            ConnectionError: If communication with the sensor is lost.
        """
        pass

    @abstractmethod
    def integrate_with_simulation(self, simulation_data: Dict[str, Any]) -> Dict[str, Any]:
        """Integrate sensor data with the current simulation state.
        
        This method takes the current simulation state and sensor readings to
        produce updated simulation parameters or validation data. It serves as
        the bridge between real-world sensor measurements and the physics simulation,
        enabling sensor-informed simulation or real-time validation.
        
        Args:
            simulation_data: Dictionary containing current simulation state including
                position, velocity, acceleration, forces, and other relevant physics
                parameters that the sensor data should influence or validate.
        
        Returns:
            Dict[str, Any]: Updated simulation parameters or additional data that
                incorporates sensor measurements. This may include corrected values,
                validation metrics, or new parameters derived from sensor fusion.
                
        Raises:
            IntegrationError: If sensor data cannot be properly integrated with
                simulation state due to incompatible formats or values.
        """
        pass

    @abstractmethod
    def cleanup(self) -> None:
        """Cleanup sensor resources and close hardware connections.
        
        This method handles proper shutdown of the sensor, including closing
        communication channels, releasing hardware resources, and performing
        any necessary cleanup operations to leave the sensor in a safe state.
        
        Should be called when the sensor is no longer needed or before
        application shutdown to ensure proper resource management.
        
        Raises:
            SensorError: If cleanup operations fail, though this should not
                prevent the application from continuing its shutdown process.
        """
        pass

    def is_connected(self) -> bool:
        """Check if the sensor is currently connected and responsive.
        
        This optional method provides a way to verify sensor connectivity
        without performing a full data read operation. Useful for health
        monitoring and error detection.
        
        Returns:
            bool: True if sensor is connected and responsive, False otherwise.
        """
        return False

    def get_sensor_info(self) -> Dict[str, str]:
        """Get sensor information and capabilities.
        
        This optional method returns metadata about the sensor including
        model, capabilities, supported data types, and other descriptive
        information useful for debugging and system documentation.
        
        Returns:
            Dict[str, str]: Dictionary containing sensor metadata such as
                'model', 'manufacturer', 'version', 'capabilities', etc.
        """
        return {
            'model': 'Unknown',
            'manufacturer': 'Unknown',
            'version': 'Unknown',
            'capabilities': 'Unknown'
        }