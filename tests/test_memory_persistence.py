import os
import subprocess
import sys

def test_configured_memory_survives_new_process(tmp_path):
    db = tmp_path / "persistent" / "memory.db"
    env = dict(os.environ, IAPUTA_MEMORY_DB_PATH=str(db))
    module = "app.application.use_cases.memory_service"
    subprocess.run([sys.executable, "-c", f"from {module} import save_message; save_message('user', 'persistence-test')"], env=env, check=True)
    subprocess.run([sys.executable, "-c", f"from {module} import get_recent_history; assert get_recent_history() == [dict(role='user', content='persistence-test')]"], env=env, check=True)
    assert db.is_file()
