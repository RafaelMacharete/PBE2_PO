import styles from './Initial.module.css'
import { Header } from '../components/Header'
import { Aside } from '../components/Aside'
import { Main } from '../components/Main'
import { Footer } from '../components/Footer'
import { Outlet } from 'react-router'

export function Initial() {
    return (
        <div className={styles.grid_container}>
            <Header/>
            
            <Aside />
            
            {/* <Main /> */}
            <Outlet />
            
            <Footer />

        </div>
    )
}