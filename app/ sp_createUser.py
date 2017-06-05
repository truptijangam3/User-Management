
cursor.callproc('sp_createUser',(_name,_email,_hashed_password))
data = cursor.fetchall()
 
if len(data) is 0:
    conn.commit()
    return json.dumps({'message':'User created successfully !'})
else:
    return json.dumps({'error':str(data[0])})



DELIMITER $$
CREATE DEFINER=`root`@`localhost` PROCEDURE `sp_createUser`(
    
    IN p_name VARCHAR(45),
    IN p_username VARCHAR(45),
    IN p_password VARCHAR(45),
    IN p_confirm_password VARCHAR(45),
    IN p_DD VARCHAR(2),
    IN p_MM VARCHAR(20),
    IN p_YYYY VARCHAR(4),
    IN p_mobile_number VARCHAR(10),
    IN p_location VARCHAR(20),
    
)
BEGIN
    if ( select exists (select 1 from tbl_user where user_username = p_username) ) THEN
     
        select 'Username Exists !!';
     
    ELSE
     
        insert into tbl_user
        (
            user_name,
            user_username,
            user_password,
            user_confirm_passwod,
            user_DD,
            user_MM,
            user_YYYY,
            user_mobile_number,
            user_location
        )
        values
        (
            p_name,
            p_username,
            p_password,
            p_confirm_passwod,
            p_DD,
            p_MM,
            p_YYYY,
            p_mobile_number,
            p_location

        );
     
    END IF;
END$$
DELIMITER ;
