import speedtest

def run_speed_test():
    st = speedtest.Speedtest()

    print("Finding the best server...")
    st.get_best_server()

    print("Performing download test...")
    download_speed = st.download() / 1_000_000  # Convert from bits/s to Mbits/s

    print("Performing upload test...")
    upload_speed = st.upload() / 1_000_000  # Convert from bits/s to Mbits/s

    ping = st.results.ping

    print(f"Download speed: {download_speed:.2f} Mbps")
    print(f"Upload speed: {upload_speed:.2f} Mbps")
    print(f"Ping: {ping:.2f} ms")

if __name__ == "__main__":
    run_speed_test()
