import styles from './Contador.module.css';
import { useState } from 'react'

export function Counter() {

    const [value, setValue] = useState(0);


    function incrementValue() {
        setValue(value + 1);
    };

    function decrementValue(){
        setValue(value - 1);
    }

    return (
        <div className={styles.container}>
            <h1 className={styles.title}>Contador</h1>

            <div className={styles.button_container}>

                <button
                    className={styles.button}
                    onClick={incrementValue}
                >+
                </button>

                <p
                    className={styles.value}
                >{value}
                </p>

                <button
                    className={styles.button}
                    onClick={decrementValue}
                >-</button>
            </div>

        </div>
    )
};