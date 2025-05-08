// import styles from './Login.module.css'
import styles from './principal.module.css'
import { useForm } from 'react-hook-form'
import { z } from 'zod'
import { zodResolver } from '@hookform/resolvers/zod'
import { useNavigate } from 'react-router'

const loginSchema = z.object({
    email: z.string().email({ message: 'Insert a valid email' }),
    password: z.string().min(1, { message: 'Password is a required field' })
})

export function Login() {
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
            <p className={styles.title}>Login</p>

            <form onSubmit={handleSubmit(handleLogin)} className={styles.form}>
                <input
                    {...register('email')}
                    placeholder='E-mail'
                    className={styles.field}
                />
                {errors.email && <p className={styles.error}>{errors.email.message}</p>}

                <input
                    {...register('password')}
                    placeholder='Password'
                    type='password'
                    className={styles.field}
                />
                {errors.password && <p className={styles.error}>{errors.password.message}</p>}

                <button type='submit' className={styles.button}>
                    Login
                </button>
            </form>
        </div>
    )
}
