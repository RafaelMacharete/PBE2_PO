import styles from './Basis.module.css'
import { Button } from '../components/Button'
import { Counter } from '../components/Counter'
export function Basis() {
    return (
        <div className={styles.container}>
            <p className={styles.title}>Basis</p>
            <h2 className={styles.props}>Props</h2>
            <div className={styles.containerButtons}>
                <Button 
                title='Login'
                act={() => alert('Você clicou no Login')}
                />
                
                <Button 
                title='Register'
                act={() => alert('Você clicou no Register')}
                />
                
                <Button 
                title='Sign out'
                act={() => alert('VocÊ clicou no Sign out')}
                />
                
                <Button 
                title='Ot'
                act={() => alert('Você clicou no Ot')}
                />
            </div>

            <Counter />
        </div>
    )
}