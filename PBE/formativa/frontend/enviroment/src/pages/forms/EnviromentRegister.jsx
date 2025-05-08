// import styles from './EnviromentRegister.module.css'
import styles from './principal.module.css'
import { useForm } from 'react-hook-form'
import { z } from 'zod'
import { zodResolver } from '@hookform/resolvers/zod'
import { useNavigate } from 'react-router'

const loginSchema = z.object({
    description: z.string().min(2,{ message: 'Description must containt at least 2 characters' }),
    location: z.string().min(2, { message: 'Location must containt at least 2 characters' })
})

export function EnviromentRegister() {
    const navigate = useNavigate()

    const { register, handleSubmit, formState: { errors } } = useForm({
        resolver: zodResolver(loginSchema)
    })

    function handleLogin(data) {
        console.log(data)
        navigate('initial')
    }

    return (
        <div className={styles.container}>
            <p className={styles.title}>Enviroment Register</p>

            <form onSubmit={handleSubmit(handleLogin)} className={styles.form}>
                <input
                    {...register('description')}
                    placeholder='Description'
                    className={styles.field}
                />
                {errors.description && <p className={styles.error}>{errors.description.message}</p>}

                <input
                    {...register('location')}
                    placeholder='Location'
                    className={styles.field}
                />
                {errors.location && <p className={styles.error}>{errors.location.message}</p>}

                <button type='submit' className={styles.button}>
                    Login
                </button>
            </form>
        </div>
    )
}
