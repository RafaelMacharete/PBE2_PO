// import styles from './Booking.module.css'
import styles from './principal.module.css'
import { useForm } from 'react-hook-form';
import { z } from 'zod';
import { zodResolver } from '@hookform/resolvers/zod';

const loginSchema = z.object({
    startDate: z.string().min(2, { message: 'Insert a subject' }),
    endDate: z.string().min(2, { message: 'Insert a subject' }),
    period: z.string().min(2, { message: 'Insert a subject' }),
    reservedClass: z.string().min(1, { message: 'Insert a valid reserved class' }),
    teacher: z.string().min(3, { message: 'Insert a valid teacher' }),
    subjectAssociated: z.string().min(2, { message: 'Insert a subject' }),
})

export function Booking() {
    const { register, handleSubmit, formState: { errors } } = useForm({
        resolver: zodResolver(loginSchema)
    })

    function userAutenticate(data) {
        console.log(data)
    }

    return (
        <div className={styles.container}>
            <p className={styles.title}>Booking</p>

            <form
                onSubmit={handleSubmit(userAutenticate)}
                className={styles.form}
            >
                <input
                    {...register('startDate')}
                    placeholder='Start Date'
                    className={styles.field}
                />
                {errors.startDate && (<p>{errors.startDate.message}</p>)}

                <input
                    {...register('endDate')}
                    placeholder='End Date'
                    className={styles.field}
                    />
                {errors.endDate && (<p>{errors.endDate.message}</p>)}
                <input
                    {...register('period')}
                    placeholder='Period'
                    className={styles.field}
                    />
                {errors.period && (<p>{errors.period.message}</p>)}
                <input
                    {...register('reservedClass')}
                    placeholder='Reserved Class'
                    className={styles.field}
                    />
                {errors.reservedClass && (<p>{errors.reservedClass.message}</p>)}
                <input
                    {...register('subjectAssociated')}
                    placeholder='Subject Associated'
                    className={styles.field}
                    />
            {errors.subjectAssociated && (<p>{errors.subjectAssociated.message}</p>)}
                <button
                    type='submit'
                    className={styles.button}
                >Login</button>
            </form>
        </div>
    );
}
