import styles from './Button.module.css'

export function Button({ title, act }) {
    return (
        <button
            onClick={act}
            className={styles.button}
        >{title}
        </button>
    )
}