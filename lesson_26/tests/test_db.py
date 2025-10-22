import main


def test_db_operations():
    main.create_table()

    # Insert
    user_id = main.insert_user("Vasyl")
    assert user_id is not None

    # Select
    users = main.get_users()
    assert any(u[1] == "Vasyl" for u in users)

    # Update
    main.update_user(user_id, "Petro")
    users = main.get_users()
    assert any(u[1] == "Petro" for u in users)

    # Delete
    main.delete_user(user_id)
    users = main.get_users()
    assert all(u[0] != user_id for u in users)
