# Xbox Controller Viewer

A real-time web-based visualization tool for Xbox controller inputs using Flask, SocketIO, and HTML5. This application provides a visual representation of controller button presses and analog stick movements through an intuitive web interface.

## Features

- Real-time visualization of Xbox controller inputs
- Support for:
  - A, B, X, Y buttons with color-coded feedback
  - Left and right analog sticks with position tracking
  - Visual feedback for button presses
- Debug console showing detailed controller events
- Start/Stop functionality for controller monitoring
- Cross-platform compatibility

## Prerequisites

- Python 3.x
- Xbox controller (or compatible gamepad)
- Modern web browser

## Installation

1. Clone the repository:
```bash
git clone [repository-url]
cd xbox-controller-viewer
```

2. Install the required Python packages:
```bash
pip install flask flask-socketio inputs
```

## Usage

1. Start the server:
```bash
python controller-Vtest.py
```

2. Open your web browser and navigate to:
```
http://localhost:5000
```

3. Click the "Start Controller" button to begin monitoring controller inputs
4. Connect your Xbox controller if not already connected
5. Interact with your controller to see real-time visualization

## Technical Details

- **Backend**: Flask + SocketIO for real-time communication
- **Frontend**: HTML5, CSS3, JavaScript
- **Controller Input**: Python `inputs` library for gamepad event handling
- **Communication**: WebSocket protocol for low-latency updates

## Troubleshooting

- If no gamepad is detected, ensure your controller is properly connected
- The application will automatically notify you if the controller gets disconnected
- Check the debug console in the web interface for detailed event information

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the Creative Commons Attribution-NonCommercial 4.0 International License (CC BY-NC 4.0).

This means you are free to:
- Share — copy and redistribute the material in any medium or format
- Adapt — remix, transform, and build upon the material

Under the following terms:
- Attribution — You must give appropriate credit, provide a link to the license, and indicate if changes were made.
- NonCommercial — You may not use the material for commercial purposes.

For the full license text, visit: https://creativecommons.org/licenses/by-nc/4.0/

## Acknowledgments

- Built with Flask and SocketIO
- Uses the `inputs` Python library for controller input handling
