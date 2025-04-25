import styles from './Aside.module.css'
import userFoto from '../assets/me.png'
import { HiAcademicCap } from "react-icons/hi2";
import { ImBooks } from "react-icons/im";
import { SiGoogleclassroom } from "react-icons/si";
import { RiCalendarScheduleLine } from "react-icons/ri";
import { Link } from 'react-router';

export function Aside() {
    return (
        <aside className={styles.container}>

            <header>
                <img
                    className={styles.header_logo}
                    src={'https://images.unsplash.com/photo-1564640227760-db286729bf83?q=80&w=1836&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D'}
                    alt='flower'
                />

                <div className={styles.user_info}>
                    <img 
                    className={styles.user_image} 
                    src={userFoto}
                    alt="user image" />
                    <p className={styles.username}>Usuário</p>
                </div>
            </header>

            <section className={styles.conteiner_button}>

                <Link className={styles.button} to={'subject'}>
                    <ImBooks />
                    Subject
                </Link>

                <Link className={styles.button} to={'teacher'}>
                    <HiAcademicCap />
                    Teacher
                </Link>

                <Link className={styles.button} to={'enviroment'}>
                    <SiGoogleclassroom />
                    Enviroment
                </Link>


                <Link className={styles.button} to={''}>
                    <RiCalendarScheduleLine />
                    Booking
                </Link>

            </section>
        </aside>
    )
};