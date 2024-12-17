# https://openbci.com/forum/index.php?p=/discussion/3918/networking-widget-to-brainflow-example
import argparse
import time

from brainflow.board_shim import BoardShim, BrainFlowInputParams, BoardIds

################################################################################

def get_most_recent_sample(board: BoardShim) -> float:
    # get latest 10 or less packages. it doesn't remove them from internal buffer
    data = board.get_current_board_data(10)
    eeg_channels = BoardShim.get_eeg_channels(board.get_board_id())
    first_channel = eeg_channels[0]
    most_recent_sample = data[first_channel, -1]
    return most_recent_sample

def create_horizontal_graph(value: float, width: int = 50, min_value: int = -400, max_value: int = 400) -> str:
    range_value = max_value - min_value
    position = int((value - min_value) / range_value * width)
    position = max(0, min(position, width - 1))  # Ensure position is within bounds?
    line_graph = " " * position + "•" + " " * (width - position - 1)
    return line_graph

################################################################################

def get_args():
    parser = argparse.ArgumentParser()
    # use docs to check which parameters are required for specific board, e.g. for Cyton - set serial port
    parser.add_argument('--timeout', type=int, help='timeout for device discovery or connection', required=False,
                        default=0)
    parser.add_argument('--ip-port', type=int, help='ip port', required=False, default=0)
    parser.add_argument('--ip-protocol', type=int, help='ip protocol, check IpProtocolType enum', required=False,
                        default=0)
    parser.add_argument('--ip-address', type=str, help='ip address', required=False, default='')
    parser.add_argument('--serial-port', type=str, help='serial port', required=False, default='/dev/cu.usbserial-DP04WFX7')
    parser.add_argument('--mac-address', type=str, help='mac address', required=False, default='')
    parser.add_argument('--other-info', type=str, help='other info', required=False, default='')
    parser.add_argument('--serial-number', type=str, help='serial number', required=False, default='')
    parser.add_argument('--board-id', type=int, help='board id, check docs to get a list of supported boards',
                        required=False, default=BoardIds.CYTON_BOARD)
    parser.add_argument('--file', type=str, help='file', required=False, default='')
    parser.add_argument('--master-board', type=int, help='master board id for streaming and playback boards',
                        required=False, default=BoardIds.NO_BOARD)
    args = parser.parse_args()

    return args

def main():
    ############################################################################
    # setup
    BoardShim.enable_dev_board_logger()

    args = get_args()
    params = BrainFlowInputParams()
    params.ip_port = args.ip_port
    params.serial_port = args.serial_port
    params.mac_address = args.mac_address
    params.other_info = args.other_info
    params.serial_number = args.serial_number
    params.ip_address = args.ip_address
    params.ip_protocol = args.ip_protocol
    params.timeout = args.timeout
    params.file = args.file
    params.master_board = args.master_board

    ############################################################################
    # get board
    board = BoardShim(args.board_id, params)

    board.prepare_session()
    board.start_stream()
    time.sleep(1)

    ############################################################################
    # get data
    for _ in range(5000):
        sample = get_most_recent_sample(board)
        graph = create_horizontal_graph(sample)
        print(graph)

        time.sleep(0.01)

    board.stop_stream()
    board.release_session()

################################################################################

if __name__ == "__main__":
    main()
