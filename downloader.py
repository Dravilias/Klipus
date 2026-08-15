import asyncio
import os
import time

download_dir = "/tmp/klipus"
timeout = 60 # seconds

async def download_medal(url) :
    os.makedirs(download_dir, exist_ok=True)

    timestamp = int(time.time());
    output_path = os.path.join(download_dir, f"{timestamp}.%(ext)s");

    proc = await asyncio.create_subprocess_exec(
        "python", "-m", "yt_dlp",
        "--no-playlist",
        "-o", output_path,
        url,

        stdout = asyncio.subprocess.PIPE, # stuff out
        stderr = asyncio.subprocess.PIPE # error out
    )

    try:
        stdout, stderr = await asyncio.wait_for(proc.communicate(), timeout=timeout)
    except asyncio.TimeoutError:
        proc.kill()
        raise Exception ("Download timed out")

    if proc.returncode != 0 :
        raise Exception(f"yt-dlp error: {stderr.decode()}")

    for filename in os.listdir(download_dir):
        if filename.startswith(str(timestamp)):
            return os.path.join(download_dir, filename)
        
    raise Exception ("file not found after download")